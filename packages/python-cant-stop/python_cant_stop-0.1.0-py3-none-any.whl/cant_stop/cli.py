from argparse import ArgumentParser
from collections import Counter
import logging
from typing import List


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def calculate_score(counts: Counter) -> int:
    """
    Calculates the score of the given set of black tokens placed during a turn of the dice game
    Can't Stop.

    :param counts: Dictionary where the keys are the number rolled and values are the number of
                   tokens placed for each number
    :type counts: Counter
    :rtype: int
    """
    score = 0

    try:
        score += sum((abs(k - 7) + 1) * (v + 1) for k, v in counts.items())
    except BaseException as exc:
        LOGGER.error("Caught {exc} while calculating base column score", exc_info=True)
        raise

    if len(counts) == 3:
        try:
            even_cols = [k % 2 for k in counts.keys()]
            if all(even_cols):
                score -= 2
            elif not any(even_cols):
                score += 2
        except BaseException as exc:
            LOGGER.error("Caught {exc} while calculating even/odd score", exc_info=True)
            raise

        try:
            if all(k > 6 for k in counts.keys()) or all (k < 8 for k in counts.keys()):
                score += 4
        except BaseException as exc:
            LOGGER.error("Caught {exc} while calculating over/under score", exc_info=True)
            raise

    return score

def parse_arglist(arglist: List[str]) -> Counter:
    return Counter(int(e.split("x")[0]) for e in arglist for _ in range(int(e.split("x")[1])))


def main():
    parser = ArgumentParser(description="Calculates Can't Stop turn scores.")
    parser.add_argument("counts", type=str, nargs="+")
    args = parser.parse_args()
    counts = parse_arglist(args.counts)
    score = calculate_score(counts)
    LOGGER.info(f"Your score is {score}")


if __name__ == "__main__":
    main()
