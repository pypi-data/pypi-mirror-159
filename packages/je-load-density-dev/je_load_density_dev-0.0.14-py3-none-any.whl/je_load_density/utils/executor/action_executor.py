import sys
import types

from je_load_density.utils.exception.exception import LoadDensityTestExecuteException
from je_load_density.utils.exception.exception_tag import executor_data_error, add_command_exception_tag
from je_load_density.utils.exception.exception_tag import executor_list_error
from je_load_density.utils.html_report.html_report_generate import generate_html
from je_load_density.utils.json.json_file.json_file import read_action_json
from je_load_density.wrapper.env_with_user.wrapper_env_and_user import loading_test_with_user


class Executor(object):

    def __init__(self):
        self.event_dict = {
            "loading_test_with_user": loading_test_with_user,
            "generate_html": generate_html,
        }

    def _execute_event(self, action: list):
        """
        :param action: execute action
        :return: what event return
        """
        event = self.event_dict.get(action[0])
        if len(action) == 2:
            return event(**action[1])
        elif len(action) == 1:
            return event()
        else:
            raise LoadDensityTestExecuteException(executor_data_error)

    def execute_action(self, action_list: list) -> dict:
        """
        :param action_list: like this structure
        [
            ["method on event_dict", {"param": params}],
            ["method on event_dict", {"param": params}]
        ]
        for loop and use execute_event function to execute
        :return: recode string, response as list
        """
        execute_record_dict = dict()
        try:
            if len(action_list) > 0 or type(action_list) is list:
                pass
            else:
                raise LoadDensityTestExecuteException(executor_list_error)
        except Exception as error:
            print(repr(error), file=sys.stderr)
        for action in action_list:
            try:
                event_response = self._execute_event(action)
                execute_record = "execute: " + str(action)
                execute_record_dict.update({execute_record: event_response})
            except Exception as error:
                print(repr(error), file=sys.stderr)
        return execute_record_dict

    def execute_files(self, execute_files_list: list):
        """
        :param execute_files_list: list include execute files path
        :return: every execute detail as list
        """
        execute_detail_list = list()
        for file in execute_files_list:
            execute_detail_list.append(self.execute_action(read_action_json(file)))
        return execute_detail_list


executor = Executor()


def add_command_to_executor(command_dict: dict):
    for command_name, command in command_dict.items():
        if isinstance(command, (types.MethodType, types.FunctionType)):
            executor.event_dict.update({command_name: command})
        else:
            raise LoadDensityTestExecuteException(add_command_exception_tag)


def execute_action(action_list: list) -> dict:
    return executor.execute_action(action_list)


def execute_files(execute_files_list: list) -> list:
    return executor.execute_files(execute_files_list)
