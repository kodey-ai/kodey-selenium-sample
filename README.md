# kodey-selenium-sample

This repository is an example Kodey.ai Coding Agent Workflow

## Objectives

In this sample, we will explore how Kodey.ai can create selenium code and automate it.

## Project Setup & Steps 

1. Signup for a new Kodey.ai account or login to your existing Kodey.ai environmenty (link-here)
2. Configure your Kodey.ai integrations to the desired issue tracker and cloud git provider.
3. Fork this repository, and clone it to the cloud git provider of your choosing (Github, Azure DevOps, Bitbucket)
4. Create the sample issue / work item in your issue tracker. Copy and Paste the issue description from below.
5. Execute the below prompt in the Kodey.ai chat UI
6. Validate the commits and pull requests in your cloud git provider

### SAMPLE PROMPT - Github Tools (Crawling Quotes To Scrape Website and getting data)
```
    branch name to create: feature/quotes-to-scrape

    Information to agent: Do as the steps below are defined one by one. You are working in github repo so make sure to use tools related to github repo.
    NOTE: You should write the actual implementation of code not just comments. 
    
    Steps:

    step 1: Using GithubCreateNewBranch tool, Create a new branch with name <branch name to create> first and then do the steps below.

    step 2: Using WebCrawler Tool, understand how to use selenium and webdriver_manager to initiate a driver in headless mode and scrape data from
    https://www.scrapingbee.com/blog/selenium-python/

    step 3: Using GithubCreateNewFile tool, Create a new file called driver.py, the file should have class and methods to initiate a chrome driver.
    The driver should be in headless mode. The class should have a method to get the driver instance and another method to close the driver instance.
    The class should be named as Driver and the file should be in the root directory of the repository. You have to use webdriver_manager to initiate the driver.
    Make sure to use the chrome driver.

    step 4: Using GithubCreateNewFile tool, Create another new file called scrapers/quotes_to_scrape.py, the file should use the driver instance created in the previous step.
    This new file should have a class and methods to scrape quotes from the website http://quotes.toscrape.com/. THe file should scrape qutoes, authors and tags. Below are the CSS selectors to be used:
    quote: div.quote > span.text
    author: div.quote > span small.author
    tags: div.quote > div.tags a.tag
    NOTE: The output should be a list of dictionaries with keys as quote, author and tags and should be saved in a json file.

    step 5: Using GithubCreateNewFile tool, Create a new file called main.py which should use the driver and scrapers/quotes_to_scrape.py to scrape the quotes details and print them.

    step 6: Using GithubCreateNewFile tool, cerate a new file called requirements.txt and add the packages required to run the code.
    
    step 7: Using GithubCreatePullRequest tool, create a new Pull Request from the above created branch with title "Added Quotes To Scrape".
```

### SAMPLE PROMPT - Azure DevOps Tools (Crawling Quotes To Scrape Website and getting data)
```
    branch name to create: feature/quotes-to-scrape

    Information to agent: Do as the steps below are defined one by one. You are working in azure repo so make sure to use tools related to azure repo.
    NOTE: You should write the actual implementation of code not just comments. 
    
    Steps:

    step 1: Using AzureDevopsBranchesCreateBranch tool, Create a new branch with name <branch name to create> first and then do the steps below.

    step 2: Using WebCrawler Tool, understand how to use selenium and webdriver_manager to initiate a driver in headless mode and scrape data from
    https://www.scrapingbee.com/blog/selenium-python/

    step 3: Using AzureDevopsRepositoryCreateNewFile tool, Create a new file called driver.py, the file should have class and methods to initiate a chrome driver.
    The driver should be in headless mode. The class should have a method to get the driver instance and another method to close the driver instance.
    The class should be named as Driver and the file should be in the root directory of the repository. You have to use webdriver_manager to initiate the driver.
    Make sure to use the chrome driver.

    step 4: Using AzureDevopsRepositoryCreateNewFile tool, Create another new file called scrapers/quotes_to_scrape.py, the file should use the driver instance created in the previous step.
    This new file should have a class and methods to scrape quotes from the website http://quotes.toscrape.com/. THe file should scrape qutoes, authors and tags. Below are the CSS selectors to be used:
    quote: div.quote > span.text
    author: div.quote > span small.author
    tags: div.quote > div.tags a.tag
    NOTE: The output should be a list of dictionaries with keys as quote, author and tags and should be saved in a json file.

    step 5: Using AzureDevopsRepositoryCreateNewFile tool, Create a new file called main.py which should use the driver and quotes-to-scrape.py to scrape the quotes details and print them.

    step 6: Using AzureDevopsRepositoryCreateNewFile tool, cerate a new file called requirements.txt and add the packages required to run the code.
    
    step 7: Using AzureDevopsPullRequestsCreatePullRequest tool, create a new Pull Request from the above created branch with title "Added Quotes To Scrape".

    step 8: Using AzureDevopsIssuesUpdateIssue tool, update the issue status to done.
```

### SAMPLE PROMPT - Jira / Bitbucket (Crawling Quotes To Scrape Website and getting data)
```

   branch name to create: feature/quotes-to-scrape

    Information to agent: Do as the steps below are defined one by one. You are working in azure repo so make sure to use tools related to azure repo.
    NOTE: You should write the actual implementation of code not just comments. 
    
    Steps:

    step 1: Using BitBucketCreateNewBranch tool, Create a new branch with name <branch name to create> first and then do the steps below.

    step 2: Using WebCrawler Tool, understand how to use selenium and webdriver_manager to initiate a driver in headless mode and scrape data from
    https://www.scrapingbee.com/blog/selenium-python/

    step 3: Using BitBucketWriteCode tool, Create a new file called driver.py, the file should have class and methods to initiate a chrome driver.
    The driver should be in headless mode. The class should have a method to get the driver instance and another method to close the driver instance.
    The class should be named as Driver and the file should be in the root directory of the repository. You have to use webdriver_manager to initiate the driver.
    Make sure to use the chrome driver.

    step 4: Using BitBucketWriteCode tool, Create another new file called scrapers/quotes_to_scrape.py, the file should use the driver instance created in the previous step.
    This new file should have a class and methods to scrape quotes from the website http://quotes.toscrape.com/. THe file should scrape qutoes, authors and tags. Below are the CSS selectors to be used:
    quote: div.quote > span.text
    author: div.quote > span small.author
    tags: div.quote > div.tags a.tag
    NOTE: The output should be a list of dictionaries with keys as quote, author and tags and should be saved in a json file.

    step 5: Using BitBucketWriteCode tool, Create a new file called main.py which should use the driver and quotes-to-scrape.py to scrape the quotes details and print them.

    step 6: Using BitBucketWriteCode tool, cerate a new file called requirements.txt and add the packages required to run the code.
    
    step 7: Using BitBucketCreateNewPullRequest tool, create a new Pull Request from the above created branch with title "Added Quotes To Scrape".

    step 8: Update this jira issue status to done.
```

## Once you have set the description of the issue in your relavant system. You need to use kodey UI Chat and execute below statement to get the work done. 

### Github Issue and Github Repo
```
   Get the issue with id <issue_id> from github repo and do as the description of the issue says.
```

### Azure Repo Issue and Azure Repo
```
   Get the issue with id <issue_id> from azure repo and do as the description of the issue says.
```

### Jira Issue and Bitbucket Repo
```
   Get the issue with id <issue_id> from jira and do as the description of the issue says.
```

## Confirming Successful Sample Outputs

1. Confirm that the branch was created on the issue / work item
2. Confirm that the code created in the associated pull request contains the following
3. Confirm that the work item/issue/ticket in your relevant issue tracking platform is updated.