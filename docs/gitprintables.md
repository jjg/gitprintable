# gitprintables
A search engine that indexes printable models (and their associated repositories) stored on Github.

## Problem
Many people are creating 3d printable models and most are sharing them.  However, the way these are usually shared are through centralized, proprietary websites owned by printer maufacturers.  This is a problem because the owners of these websites claim some degree of ownership over the designs, and they also mediate access to them.  Because of this some designers have taken to sharing their work via Github, but at the moment there is no unified interface for browsing or searching for these models.

## Solution
Create a web crawler which periodically crawls the Github website (via traditional http means or by using the Github API) and indexes projects which contain 3d model files.  Provide a web interface to browse and search the data collected by the crawling process.

## Implementation

### Crawler

Steps (first pass):
1.  Get a list of repositories 
2.  Get a list of files
3.  Search files for known 3D model types (initially `.stl`, .`scad`)
4.  Add repositories with matching files to second indexing pass queue

Steps (second pass):
1.  Add repository to index
2.  Ingest README
3.  Ingest 3d model files
4.  Assign/request webhook to automate updates

### User Interface

The user interface consists of a simple search box and a browseable directory.  Text entered into the search box first queries the contents of the README documents stored in the index, then queries the list of printable files by name to find matches.

The browse feature generates a browsable tree structure based on any categorical data that can be extracted from the files themselves or deduced from the README files.  This is a bit tricker to implement and will require some experimentation to determine how effective it can be.

Search results link to a summary view which presents an interactive 3D rendering of the selected model along with any same-named image files (A guess that they might be photos of the model).  The README for the repository is also displayed along with a link back to the repository on Github.  Additional statistical information may be included if it's useful

## Bonus Beats
*  Be compatible with all git repositories and don't rely on Github-specific API's, etc.
*  Notify repository owners when their project is included in the index
*  Setup (or request) a webhook to each included respository to allow immediate updates of the index
*  Define a metadata standard repository owners can provide to improve the performance of the index

## Notes

This `curl` command seems to fetch files from repositories which have an extension of `.stl`:

    curl -u "username" "https://api.github.com/search/code?q=stl+in:extension"

It requires authentication, which according to the docs is true for any search against code.
