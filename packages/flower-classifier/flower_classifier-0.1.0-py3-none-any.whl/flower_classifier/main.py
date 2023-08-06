from argparse import Namespace

from configs.config import parse_arguments
from orchestrate import Orchestrator

args: Namespace = parse_arguments()


def main():
    orchestrator = Orchestrator(run_mode=args.run_mode)

    orchestrator.run()


if __name__ == '__main__':
    main()
