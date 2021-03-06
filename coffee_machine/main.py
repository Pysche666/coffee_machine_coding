import logging
import sys

from coffee_machine.apputils import create_logger
from coffee_machine.data.process_input import get_machine_configuration
from coffee_machine.coffee_system import CoffeeMachine

logger = logging.getLogger()


def main():
    # create a log file
    global logger
    logger = create_logger()

    # get user input
    if len(sys.argv) != 2:
        logger.info("correct usage is :: python3 main.py <user_input>.json\n exiting...")
        exit(0)
    # json file
    user_input_file = sys.argv[1]
    # load machine configuration from user input file
    machine_config = get_machine_configuration(user_input_file)
    my_coffee_machine = CoffeeMachine(machine_config)
    # start the machine
    my_coffee_machine.run()


if __name__ == '__main__':
    main()
