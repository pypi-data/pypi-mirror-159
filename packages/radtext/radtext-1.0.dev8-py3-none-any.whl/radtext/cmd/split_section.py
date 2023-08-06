"""
Usage:
    split_section regex [--overwrite] --section-titles FILE -i FILE -o FILE
    split_section medspacy [--overwrite] -i FILE -o FILE

Options:
    --section-titles FILE   List of section titles [default: .radtext/resources/section_titles.txt]
    -o FILE
    -i FILE
    --overwrite
"""
import bioc
import docopt

from radtext.cmd.cmd_utils import process_options
from radtext.models.section_split.section_split_regex import BioCSectionSplitterRegex, combine_patterns


def main():
    argv = docopt.docopt(__doc__)
    process_options(argv)

    try:
        if argv['regex']:
            with open(argv['--section-titles']) as fp:
                section_titles = [line.strip() for line in fp]
            pattern = combine_patterns(section_titles)
            processor = BioCSectionSplitterRegex(regex_pattern=pattern)
        elif argv['medspacy']:
            import medspacy
            from radtext.models.section_split.section_split_medspacy import BioCSectionSplitterMedSpacy
            nlp = medspacy.load(enable=["sectionizer"])
            processor = BioCSectionSplitterMedSpacy(nlp)
        else:
            raise KeyError
    except KeyError as e:
        raise e

    with open(argv['-i']) as fp:
        collection = bioc.load(fp)

    processor.process_collection(collection)

    with open(argv['-o'], 'w') as fp:
        bioc.dump(collection, fp)


if __name__ == '__main__':
    main()
