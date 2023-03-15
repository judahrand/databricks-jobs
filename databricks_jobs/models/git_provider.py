from enum import Enum


class GitProvider(str, Enum):
    GITHUB = "gitHub"
    BITBUCKETCLOUD = "bitbucketCloud"
    AZUREDEVOPSSERVICES = "azureDevOpsServices"
    GITHUBENTERPRISE = "gitHubEnterprise"
    BITBUCKETSERVER = "bitbucketServer"
    GITLAB = "gitLab"
    GITLABENTERPRISEEDITION = "gitLabEnterpriseEdition"
    AWSCODECOMMIT = "awsCodeCommit"

    def __str__(self) -> str:
        return str(self.value)
