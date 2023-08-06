import importlib
import os
import re
import sys
import yaml
import tempfile
import traceback


from furl import furl

import git

from efemarai.dataset import DatasetFormat, DatasetStage
from efemarai.problem_type import ProblemType

from rich.console import Console

console = Console()


class DefinitionChecker:
    def __init__(self):
        pass

    def run(
        self,
        filename=None,
        definition=None,
        check_project=False,
        check_models=False,
        check_datasets=False,
        check_domains=False,
        check_all=False,
    ):
        try:
            if definition is None:
                definition = self._load_definition(filename)

            if check_project or check_all:
                self._check_project(definition)

            if check_datasets or check_all:
                self._check_datasets(definition)

            if check_models or check_all:
                self._check_models(definition)

        except AssertionError:
            return False

    def _error(self, message, print_exception=False):
        console.print(f":poop: {message}", style="red")

        if print_exception:
            traceback.print_exc()

        raise AssertionError()

    def _load_definition(self, filename):
        if not os.path.isfile(filename):
            self._error(f"File '{filename}' does not exist")

        with open(filename) as f:
            contents = f.read()
        contents = os.path.expandvars(contents)

        unknown_environment_variables = list(
            re.findall("\$\{([a-zA-Z]\w*)\}", contents)
        )
        if unknown_environment_variables:
            for match in unknown_environment_variables:
                self._error(
                    f"Unknown environment variable '{match}' in '{filename}'"
                )

        return yaml.safe_load(contents)

    def _get_required_item(self, definition, key, parent=None):
        item = definition.get(key)

        if item is None:
            message = f"Missing field '{key}'"
            if parent is not None:
                message += f" (in '{parent}')"
            self._error(message)

        return item

    def _check_project(self, definition):
        project = self._get_required_item(definition, "project")

        name = self._get_required_item(project, "name", "project")

        problem_type = self._get_required_item(project, "problem_type", "project")

        if not ProblemType.has(problem_type):
            self._error(f"Unsupported problem type '{problem_type}' (in 'project')")

    def _check_datasets(self, definition):
        datasets = self._get_required_item(definition, "datasets")

        if not isinstance(datasets, list):
            self._error(f"'datasets' must be an array")

        known_datasets = set()

        for i, dataset in enumerate(datasets):
            parent = f"datasets[{i}]"

            name = self._get_required_item(dataset, "name", parent)

            if name in known_datasets:
                self._error(f"Multiple datasets named '{name}' exist (in 'datasets')")

            known_datasets.add(name)

            format = self._get_required_item(dataset, "format", parent)
            if not DatasetFormat.has(format):
                self._error(
                    f"Unsupported dataset format '{format}' (in '{parent}')"
                )

            stage = self._get_required_item(dataset, "stage", parent)
            if not DatasetStage.has(stage):
                self._error(
                    f"Unsupported dataset stage '{stage}' (in '{parent}')"
                )

            upload = dataset.get("upload", False)

            if upload:
                annotations_url = dataset.get("annotations_url")
                if annotations_url is not None and not os.path.exists(annotations_url):
                    self._error(f"File path '{anotations_url}' does not exist (in '{parent}')")

                data_url = dataset.get("data_url")
                if data_url is not None and not os.path.exists(data_url):
                    self._error(f"File path '{data_url}' does not exist (in '{parent}')")

    def _check_models(self, definition):
        models = self._get_required_item(definition, "models")

        if not isinstance(models, list):
            self._error(f"'models' must be an array")

        known_models = set()

        for i, model in enumerate(models):
            parent = f"models[{i}]"
            name = self._get_required_item(model, "name", parent)

            if name in known_models:
                self._error(f"Multiple models named '{name}' exist (in 'models')")

            known_models.add(name)

            self._check_repository(model, parent)
            self._check_files(model, parent)
            self._check_runtime(model, parent)

    def _check_repository(self, model, parent):
        repository = self._get_required_item(model, "repository", parent)

        repo_parent = parent + ".repository"

        url = self._get_required_item(repository, "url", repo_parent)
        branch = repository.get("branch")
        hash = repository.get("hash")
        access_token = repository.get("access_token")

        if branch is None and hash is None:
            self._error(f"'branch' or 'hash' must be provided (in '{repo_parent}')")

        class Progress(git.remote.RemoteProgress):
            def update(self, op_code, cur_count, max_count=None, message=""):
                console.print(f"Git clone: {self._cur_line}")

        with tempfile.TemporaryDirectory() as temp_dir:
            with console.status(f"Fetching repository... (in '{repo_parent}')", spinner_style="green"):
                try:
                    clone_url = furl(url)
                    clone_url.username = access_token
                    clone_url.password = "x-oauth-basic"

                    repo = git.Repo.clone_from(
                        clone_url.tostr(),
                        temp_dir,
                        branch=branch,
                        depth=1,
                        single_branch=True,
                        # progress=Progress(),
                    )
                except Exception:
                    self._error(f"Unable to clone repository at '{url}' (in '{repo_parent}')")

            if hash is not None:
                try:
                    repo.commit(hash)
                except git.exc.GitError as e:
                    self._error(f"Commit '{hash}' does not exist (in '{repo_parent}')")

    def _check_files(self, model, parent):
        files = model.get("files", [])
        known_files = set()
        for i, file in enumerate(files):
            file_parent = parent + f".files[{i}]"
            name = self._get_required_item(file, "name", file_parent)

            if name in known_files:
                self._error(f"Multiple files named '{name}' exist (in '{parent}')")

            known_files.add(name)

            url = self._get_required_item(file, "url", parent + f".files[{i}]")

            if file.get("upload", False) and not os.path.exists(url):
                self._error(f"File path '{url}' does not exist (in '{file_parent}')")

    def _check_runtime(self, model, parent):
        sys.path.append(os.getcwd())

        runtime = self._get_required_item(model, "runtime", parent)

        runtime_parent = parent + ".runtime"

        load = self._get_entrypoint("load", runtime, parent)
        predict = self._get_entrypoint("predict", runtime, parent)


    def _get_entrypoint(self, name, runtime, parent):
        definition = self._get_required_item(runtime, name, parent)
        entrypoint_parent = parent + "." + name

        entrypoint = self._get_required_item(definition, "entrypoint", entrypoint_parent)
        module_path, function_name = entrypoint.split(":")

        if not os.path.exists(f"{module_path.replace('.', '/')}.py"):
            self._error(f"Module '{module_path}' cannot be imported (in '{entrypoint_parent}')")

        try:
            module = importlib.import_module(module_path)
        except Exception as e:
            self._error(f"Unable to import '{module_path}' (in '{entrypoint_parent}')", print_exception=True)

        try:
            function = getattr(module, function_name)
        except Exception as e:
            self._error(f"Unable to load '{function_name}' (in '{entrypoint_parent}')", print_exception=True)

        return function
