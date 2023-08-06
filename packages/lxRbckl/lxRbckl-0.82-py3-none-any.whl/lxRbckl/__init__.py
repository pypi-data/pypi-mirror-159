# import <
from json import load, dump, loads

# >


def jsonLoad(

        pFile: str,
        pNew: bool = False

):
    '''  '''

    # if new file <
    # else then existing file <
    if (pNew):

        # initialize file <
        # reiterate <
        jsonDump(pFile = pFile, data = {})
        jsonLoad(pFile = pFile)

        # >

    else:

        # get file <
        # load data <
        with open(pFile, 'r') as f:

            return load(fp = f)

        # >

    # >


def jsonDump(

        pData,
        pFile: str,
        pIndent: int = 3

):
    '''  '''

    # get file <
    # dump data <
    with open(pFile, 'w') as f:

        dump(

            fp = f,
            obj = pData,
            indent = pIndent

        )

    # >


def githubSet(

        pData,
        pFile: str,
        pGithub: object,
        pRepository: str,
        pBranch: str = 'main',
        pMessage: str = 'Automated Update'

):
    '''  '''

    # get repository <
    # get content from repository <
    repository = pGithub.get_repo(pRepository)
    content = repository.get_contents(

        path = pFile,
        ref = pBranch

    )

    # >

    # update file from repository <
    repository.update_file(

        branch = pBranch,
        sha = content.sha,
        message = pMessage,
        path = content.path,
        content = str(pData).replace('\'', '\"')

    )

    # >


def githubGet(

        pFile: str,
        pGithub: object,
        pRepository: str,
        pBranch: str = 'main'

):
    '''  '''

    # try (if content exists) <
    # except (then content does not exist) <
    try:

        # get repository <
        # get content from repository <
        repository = pGithub.get_repo(pRepository)
        content = repository.get_contents(

            path = pFile,
            ref = pBranch

        )

        # >

        return loads(content.decoded_content.decode())

    except: return None

    # >


# pip3 install setuptools
# pip3 install tqdm
# pip3 install twine
# python3 setup.py bdist_wheel
# twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
