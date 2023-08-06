"""
Usage:
    neg [options] -i FILE -o FILE

Options:
    --regex_patterns FILE               [default: resources/patterns/regex_patterns.yml]
    --ngrex_patterns FILE               [default: resources/patterns/ngrex_patterns.yml]
    --overwrite
    --sort_anns
    -o FILE
    -i FILE
"""
import bioc
from radtext.core import BioCProcessor, BioCPipeline

"""
    --regex_negation FILE               [default: resources/patterns/regex_negation.yml]
    --regex_uncertainty_pre_neg FILE    [default: resources/patterns/regex_uncertainty_pre_negation.yml]
    --regex_uncertainty_post_neg FILE   [default: resources/patterns/regex_uncertainty_post_negation.yml]
    --regex_double_neg FILE             [default: resources/patterns/regex_double_negation.yml]
    --ngrex_negation FILE               [default: resources/patterns/ngrex_negation.yml]
    --ngrex_uncertainty_pre_neg FILE    [default: resources/patterns/ngrex_uncertainty_pre_negation.yml]
    --ngrex_uncertainty_post_neg FILE   [default: resources/patterns/ngrex_uncertainty_post_negation.yml]
    --ngrex_double_neg FILE             [default: resources/patterns/ngrex_double_negation.yml]
"""
import docopt
import tqdm

from radtext.cmd.cmd_utils import process_options, process_file
from radtext.models.neg.match_ngrex import NegGrexPatterns
from radtext.models.neg import NegRegexPatterns
from radtext.models.neg import NegCleanUp
from radtext.models.neg.neg import BioCNeg


def main():
    argv = docopt.docopt(__doc__)
    process_options(argv)
    regex_actor = NegRegexPatterns()
    regex_actor.load_yml2(argv['--regex_patterns'])
    ngrex_actor = NegGrexPatterns()
    ngrex_actor.load_yml2(argv['--ngrex_patterns'])

    neg_actor = BioCNeg(regex_actor=regex_actor, ngrex_actor=ngrex_actor)
    cleanup_actor = NegCleanUp(argv['--sort_anns'])
    pipeline = BioCPipeline()
    pipeline.processors = [neg_actor, cleanup_actor]

    process_file(argv['-i'], argv['-o'], pipeline, bioc.PASSAGE)


if __name__ == '__main__':
    main()
