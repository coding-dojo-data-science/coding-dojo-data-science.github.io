# Using GitHub Pages to Host Content

- Chas Benton
- 09/05/23

> I DO NOT HAVE WINDOWS INSTRUCTIONS YET ON INSTALLING RUBY AND JEKYLL



### Resources

- Jekyll documentation - https://jekyllrb.com/docs/

## Instructions

These instructions will serve as a guide on how to host your repository into github pages website using Jekyll. 

#### Prerequisites:

- Basic Javascript, HTML, CSS Knowledge
- VS Code
- Homebrew (if using Mac)
- Git
- Github Desktop
- VS Code

### Installing Needed Packages

- Install Ruby
- Install Jekyll
- Install Bundler
- Install webrick

#### INSTALLING RUBY: 

>  MAC NOTE: Mac's come preinstalled with an older version of ruby. This is NOT the version we want to use when preparing a repository for Github pages. This is a system level ruby and will not serve our purpose. We will instead install ruby through homebrew and set our PATH to use the correct Ruby

- Open a brand new terminal and type ```brew install ruby```. Let the installation complete. Once done, configure the shell environment by opening ~/.zshrc. You can open this by using TextEdit ```open -e ~/.zshrc```. Set the $PATH environment variable. Add this at the end of your ~/.zshrc file.

##### MAC INTEL: 

```
if [ -d "/usr/local/opt/ruby/bin" ]; then
  export PATH=/usr/local/opt/ruby/bin:$PATH
  export PATH=`gem environment gemdir`/bin:$PATH
fi
```



##### MAC APPLE SILICON:



```
if [ -d "/opt/homebrew/opt/ruby/bin" ]; then
  export PATH=/opt/homebrew/opt/ruby/bin:$PATH
  export PATH=`gem environment gemdir`/bin:$PATH
fi
```



Save the file. This sets the Homebrew-installed Ruby to a higher priority than the system Ruby and adds the directory used for Ruby gems.

> * **James note: my terminal said this**

```
ruby is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have ruby first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc

For compilers to find ruby you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"

For pkg-config to find ruby you may need to set:
  export PKG_CONFIG_PATH="/opt/homebrew/opt/ruby/lib/pkgconfig"
```



#### INSTALLING JEKYLL AND BUNDLER

- After installing ruby, we can install Jekyll and bundler using this command ```gem install jekyll bundler```

#### INSTALLING WEBRICK

- The latest version of Ruby does not install webrick by default. If you want to test the github page locally, then be sure to install webrick by running ```bundle add webrick```

> James got error:`Could not locate Gemfile`

## CREATING THE SITE:

- If we are starting this site from scratch, then we are going to create a brand new repository on Github. If you already have a repository you want to add github pages to, then skip to the next bullet. 

     A lot of github instructions suggest that you name the site you will be hosting on github pages as ```<user>.github.io``` or ```<organization>.github.io```. You do not have to do this. You can still name this repository anything you wish. The settings we apply will ensure this site still works. (Note: GitHub Pages sites are publicly available on the internet, even if the repository for the site is private.)

- Once your repository is created, create a local version of this by opening this repository on Github Desktop. This can be done by pressing the code button and open in github desktop. Save the local copy in your preferred folder and press save. 

- On github desktop, press repository -> open in terminal. This should open a terminal within your repository's local file location. 

- We now need to decide what publishing source we want to use for the Github pages site. You can configure your GitHub Pages site to publish when changes are pushed to a specific branch, or you can write a GitHub Actions workflow to publish your site. 

##### For publishing to a specific branch: 

- **Option A) If you chose to publish your site from a docs folder on the main branch**, create and change directories to the docs folder. This can be done by running this on the terminal: 

```
mkdir docs (Creates a new folder called docs)
cd docs (navigates to docs folder)
```

> JAMES: is this the end of optionA?



- Option B) If you chose to publish your site from the gh-pages branch, create and checkout the gh-pages branch. We are going to use --orphan to create a branch in a git init-like state on a non-new repository. (you get a new branch with no history but same files from branch you started). Run this on the terminal:

```
git checkout --orphan gh-pages #(Creates a new branch, with no history or contents, called gh-pages, and switches to the gh-ages branch)
git rm -rf #(Removes the contents from your default branch from the working directory)
```

- Command without comments:

```
git checkout --orphan gh-pages
git rm -rf 
```

- On github.com, on your repository, we are going to navigate to the Settings tab. On the left hand side, under Code and automation, we are going to click on Pages. On the "Build and deployment" section, under "Source", make sure Deploy from a branch is selected. From "None" choose the branch you want to publish from and, optionally, the specific folder for your publishing source (if you chose docs ONLY). Save your new changes. 



## Github Actions Workflow to publish your site: 

- Generally a github action means that you want to set a trigger to publish your site. Github has many preset ones you can use but some themes will require you to use this option instead. 

- On github.com, on your repository, we are going to navigate to the Settings tab. On the left hand side, under Code and automation, we are going to click on Pages. On the "Build and deployment" section, under "Source", select Github Actions. 

- GitHub will suggest several starter workflows. If you already have a workflow to publish your site, you can skip this step. Otherwise, choose one of the options to create a GitHub Actions workflow. If you'd like to create your own Github Action workflow then follow the instructions on this link 
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

> IF YOU ARE PLANNING TO ADD A USER MADE THEME TO YOUR PROJECT, DO NOT CREATE A NEW JEKYLL SITE AND INSTEAD FOLLOW THE THEME'S README INSTRUCTIONS. THEY WILL GENERALLY HAVE PRE-MADE FILES THAT YOU CAN COPY AND PASTE TO YOUR OWN PROJECT TO MAKE THE THEME WORK. 

___



- Back to your project terminal, create a new Jekyll site by running 
```jekyll new --skip-bundle``` (Creates a Jekyll site in the current directory)
We are skipping the bundle to ensure Bundler will install your dependencies to the location used by gem install. 

- Structure of the folder should look something like this: 
    ├── index.markdown
    ├── Gemfile.lock
    ├── Gemfile
    ├── about.markdown
    ├── 404.html
    ├── _site
    ├── _posts
    └── config.yml

- Open the Gemfile created (on VS Code) and comment out ```gem "jekyll"``` by adding a # in the beginning. 

### James- Questions about below

- Add the github pages gem by removing the # on the line that says ```gem "github-pages"```. Make sure it looks like this ```gem "github-pages", "~> GITHUB-PAGES-VERSION", group: :jekyll_plugin``` where GITHUB-PAGES-VERSION is the latest supported version of github pages. This can be found here https://pages.github.com/versions/. This will ensure the correct version Jekyll will be installed as a dependency of the github-pages gem.

- Save the Gemfile. 

- Optionally, edit your _config.yml file on VS Code. Where: 

    domain: my-site.github.io (if you want to force HTTPS, specify the domain without the http at the start, e.g. example.com)
    url: https://my-site.github.io (the base hostname and protocol for your site, e.g. http://example.com)

- Run ```bundle install``` so all necessary dependencies are installed on your project folder.  `JAMES: in docs folder?`

- Push all your changes to github repository. 

- Navigate back to github.com, on your repository, to settings, code and automation, and pages. After a couple of minutes, github should publish a link to your site. 

### OPTIONALLY: If you want to see your github pages site locally:
​    ** Make sure you installed webrick or you will face a bundle error 

    - After running ```bundle install``` on your project terminal, run ```bundle exec jekyll serve```. If there are not errors, this should end with a line saying "Server running..." you can preview your site on your browser by navigating to http://localhost:4000
        - If you leave the server running, each time you edit your project, in VS Code, and press save, the page can be refreshed to reflect new changes. 

## ADDING ADDITIONAL PAGES/CONTENT/BLOG TO GITHUB PAGES

- When you created a new jekyll site, loaded an index.markdown and an about.markdown. You can use both of these pages are references to build additional pages to your site. You can always create new markdown files (the .markdown and .md is read the same). Refer to the Jekyll documentation of proper naming convention for blogs, if you plan to use the site for any blogging purposes (to post updates)

    - After you create a new .md file, make sure that you have this YAML formatter at the top of the page. 
    
    ```
    ___
    layout: page
    title: "PAGE-TITLE"
    permalink: /URL-PATH
    ___
    ```
    Note on permalink: If URL of your site is https://user.github.io and your URL-PATH is /about/, your page will be located at https://user.github.io/about/

    - Below the --- you can add the rest of the content of your page using markdown language. 
    
    - There are other YAML formatter to add to the top of the page depending on your issues. For example, the nav_order will allow you to sort your pages in any specific order you'd like, starting from 1. Without this, Jekyll will post the pages alphabetically by default. For other YAML formatters that can be used, please see the Jekyll documentation. 

- Commit your changes. 

## ADDING A THEME TO GITHUB PAGES: 

- Github pages has been kind enough to provide us with a series of themes free of use. A list of supported themes are here.  https://pages.github.com/themes/

    - Github Pre-set themes: 
        - navigate to your _config.yml either on VS code or github.com. Add a new line and type ```theme: THEME-NAME```, replacing THEME-NAME with the name of the theme as shown in the README of the theme's repository. (Ex: theme: minima)
    - Jekyll themes hosted on github: 
        - navigate to your _config.yml either on VS code or github.com. Add a new line and type ```remote_theme: THEME-NAME```, replacing THEME-NAME with the name of the theme as shown in the README of the theme's repository. (Ex: remote_theme: minima)
    - User created themes: 
        - In order to add user created themes, follow the README provided in their repository. Each theme is installed uniquely with specific settings and formats. They will provide detailed instructions on how to get the theme up and running regardless of how you chose to source the site. 
        
        NOTE: IF YOU ARE INSTALLING A THEME THAT USES GITHUB ACTIONS ON A REPOSITORY WHERE YOU ALREADY RAN ```jekyll new --skip-bundle``` AND THE THEME IS NOT LOADING: 
        - Make sure that ```gem "jekyll"``` is NOT commented out and the ```gem "github-pages", "~> GITHUB-PAGES-VERSION", group: :jekyll_plugin``` IS commented out. 

