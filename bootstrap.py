  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>buildout/bootstrap/bootstrap.py at master · buildout/buildout · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="H7Kf3MNI27/H3soIv8NaM0lXuM95tgi9AxVS9BGXFdY=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-deacc71db3df368c127857126ecd56b570a8f5e7.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-27eae33da826712ee4611abc24bad3db9b24ed3c.css" media="screen" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-ad1b87fda705d87118448f87fb6a20bdb15bd841.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-845656b5edd8e0530312c4585429c5049525e37f.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="0f5f6544a9698380e11202d06f28f338">

        <link data-pjax-transient rel='permalink' href='/buildout/buildout/blob/bbfa363c836ad16555585c0d82ebc1a2de3c88b4/bootstrap/bootstrap.py'>
    <meta property="og:title" content="buildout"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/buildout/buildout"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/25b1716e7a684f3bfc888fcf3f413baa?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="Contribute to buildout development by creating an account on GitHub."/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="buildout/buildout"/>

    <meta name="description" content="Contribute to buildout development by creating an account on GitHub." />

  <link href="https://github.com/buildout/buildout/commits/master.atom" rel="alternate" title="Recent Commits to buildout:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob  vis-public env-production  ">
    <div id="wrapper">

      

      

      

      


        <div class="header header-logged-out">
          <div class="container clearfix">

            <a class="header-logo-wordmark" href="https://github.com/">
              <img alt="GitHub" class="github-logo-4x" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x.png?1360648843" />
              <img alt="GitHub" class="github-logo-4x-hover" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x-hover.png?1360648843" />
            </a>

              
<ul class="top-nav">
    <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
  <li class="search"><a href="https://github.com/search">Search</a></li>
  <li class="features"><a href="https://github.com/features">Features</a></li>
    <li class="blog"><a href="https://github.com/blog">Blog</a></li>
</ul>


            <div class="header-actions">
                <a class="button primary" href="https://github.com/signup">Sign up for free</a>
              <a class="button" href="https://github.com/login?return_to=%2Fbuildout%2Fbuildout%2Fblob%2Fmaster%2Fbootstrap%2Fbootstrap.py">Sign in</a>
            </div>

          </div>
        </div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              


<ul class="pagehead-actions">



    <li>
      <a href="/login?return_to=%2Fbuildout%2Fbuildout"
        class="minibutton js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="mini-icon mini-icon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/buildout/buildout/stargazers">
        74
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2Fbuildout%2Fbuildout"
        class="minibutton js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="mini-icon mini-icon-fork"></span>Fork
      </a>
      <a href="/buildout/buildout/network" class="social-count">
        35
      </a>
    </li>
</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-icon mega-icon-public-repo"></span>
                <span class="author vcard">
                  <a href="/buildout" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">buildout</span>
                  </a></span> /
                <strong><a href="/buildout/buildout" class="js-current-repository">buildout</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li><a href="/buildout/buildout" class="selected" highlight="repo_source repo_downloads repo_commits repo_tags repo_branches">Code</a></li>
    <li><a href="/buildout/buildout/network" highlight="repo_network">Network</a></li>
    <li><a href="/buildout/buildout/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>11</span></a></li>

      <li><a href="/buildout/buildout/issues" highlight="repo_issues">Issues <span class='counter'>44</span></a></li>

      <li><a href="/buildout/buildout/wiki" highlight="repo_wiki">Wiki</a></li>


    <li><a href="/buildout/buildout/graphs" highlight="repo_graphs repo_contributors">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/buildout/buildout/tags" class="tabnav-tab" highlight="repo_tags">Tags <span class="counter ">67</span></a></li>
    </ul>
    
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="mini-icon mini-icon-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container js-select-menu-pane">

        <div class="select-menu-modal js-select-menu-pane">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="mini-icon mini-icon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches" data-filterable-for="commitish-filter-field" data-filterable-type="substring">


              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1" rel="nofollow" title="1">1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.3/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.3" rel="nofollow" title="1.3">1.3</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.4/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.4" rel="nofollow" title="1.4">1.4</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/2/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="2" rel="nofollow" title="2">2</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/baijum-project-name-with-underscore/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="baijum-project-name-with-underscore" rel="nofollow" title="baijum-project-name-with-underscore">baijum-project-name-with-underscore</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/ctheune-buildout-parallelfetch/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="ctheune-buildout-parallelfetch" rel="nofollow" title="ctheune-buildout-parallelfetch">ctheune-buildout-parallelfetch</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/davisagli-install-optimization/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="davisagli-install-optimization" rel="nofollow" title="davisagli-install-optimization">davisagli-install-optimization</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/do3cc_exitcode/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="do3cc_exitcode" rel="nofollow" title="do3cc_exitcode">do3cc_exitcode</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/documentation/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="documentation" rel="nofollow" title="documentation">documentation</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/encolpe-escape-command/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="encolpe-escape-command" rel="nofollow" title="encolpe-escape-command">encolpe-escape-command</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/env-cache/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="env-cache" rel="nofollow" title="env-cache">env-cache</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/faassen-develop/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="faassen-develop" rel="nofollow" title="faassen-develop">faassen-develop</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/gotcha-scripts-warning/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="gotcha-scripts-warning" rel="nofollow" title="gotcha-scripts-warning">gotcha-scripts-warning</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/gotcha-timeout-cfg/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="gotcha-timeout-cfg" rel="nofollow" title="gotcha-timeout-cfg">gotcha-timeout-cfg</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/help-api/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="help-api" rel="nofollow" title="help-api">help-api</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/jim-meta-recipes/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="jim-meta-recipes" rel="nofollow" title="jim-meta-recipes">jim-meta-recipes</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target selected">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/master/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/newbery-multiple-increments/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="newbery-multiple-increments" rel="nofollow" title="newbery-multiple-increments">newbery-multiple-increments</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/svntrunk/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="svntrunk" rel="nofollow" title="svntrunk">svntrunk</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/sylvain-distribution-cache/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="sylvain-distribution-cache" rel="nofollow" title="sylvain-distribution-cache">sylvain-distribution-cache</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/tlotze-download-hard-links/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="tlotze-download-hard-links" rel="nofollow" title="tlotze-download-hard-links">tlotze-download-hard-links</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/windows/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="windows" rel="nofollow" title="windows">windows</a>
              </div> <!-- /.select-menu-item -->

              <div class="select-menu-no-results js-not-filterable">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags" data-filterable-for="commitish-filter-field" data-filterable-type="substring">

              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/zc.recipe.egg-1.3.2/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="zc.recipe.egg-1.3.2" rel="nofollow" title="zc.recipe.egg-1.3.2">zc.recipe.egg-1.3.2</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/zc.recipe.egg-1.3.1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="zc.recipe.egg-1.3.1" rel="nofollow" title="zc.recipe.egg-1.3.1">zc.recipe.egg-1.3.1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/zc.recipe.egg-1.2.2/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="zc.recipe.egg-1.2.2" rel="nofollow" title="zc.recipe.egg-1.2.2">zc.recipe.egg-1.2.2</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/zc.recipe.egg-1.1.0/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="zc.recipe.egg-1.1.0" rel="nofollow" title="zc.recipe.egg-1.1.0">zc.recipe.egg-1.1.0</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/z3c.recipe.scripts-1.0.1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="z3c.recipe.scripts-1.0.1" rel="nofollow" title="z3c.recipe.scripts-1.0.1">z3c.recipe.scripts-1.0.1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/testrunner-1.0.0b4/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="testrunner-1.0.0b4" rel="nofollow" title="testrunner-1.0.0b4">testrunner-1.0.0b4</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/testrunner-1.0.0b3/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="testrunner-1.0.0b3" rel="nofollow" title="testrunner-1.0.0b3">testrunner-1.0.0b3</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/testrunner-1.0.0b2/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="testrunner-1.0.0b2" rel="nofollow" title="testrunner-1.0.0b2">testrunner-1.0.0b2</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/egg-1.1.0b1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="egg-1.1.0b1" rel="nofollow" title="egg-1.1.0b1">egg-1.1.0b1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/egg-1.0.0b3/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="egg-1.0.0b3" rel="nofollow" title="egg-1.0.0b3">egg-1.0.0b3</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/egg-1.0.0b2/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="egg-1.0.0b2" rel="nofollow" title="egg-1.0.0b2">egg-1.0.0b2</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/egg-1.0.0/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="egg-1.0.0" rel="nofollow" title="egg-1.0.0">egg-1.0.0</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/2.0.1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="2.0.1" rel="nofollow" title="2.0.1">2.0.1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/2.0.0b2/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="2.0.0b2" rel="nofollow" title="2.0.0b2">2.0.0b2</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/2.0.0b1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="2.0.0b1" rel="nofollow" title="2.0.0b1">2.0.0b1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/2.0.0a7/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="2.0.0a7" rel="nofollow" title="2.0.0a7">2.0.0a7</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/2.0.0a6/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="2.0.0a6" rel="nofollow" title="2.0.0a6">2.0.0a6</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/2.0.0a5/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="2.0.0a5" rel="nofollow" title="2.0.0a5">2.0.0a5</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/2.0.0a4/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="2.0.0a4" rel="nofollow" title="2.0.0a4">2.0.0a4</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/2.0.0a3/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="2.0.0a3" rel="nofollow" title="2.0.0a3">2.0.0a3</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/2.0.0a1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="2.0.0a1" rel="nofollow" title="2.0.0a1">2.0.0a1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/2.0.0/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="2.0.0" rel="nofollow" title="2.0.0">2.0.0</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.7.1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.7.1" rel="nofollow" title="1.7.1">1.7.1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.7.0b1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.7.0b1" rel="nofollow" title="1.7.0b1">1.7.0b1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.7.0/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.7.0" rel="nofollow" title="1.7.0">1.7.0</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.6.3/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.6.3" rel="nofollow" title="1.6.3">1.6.3</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.6.2/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.6.2" rel="nofollow" title="1.6.2">1.6.2</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.6.1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.6.1" rel="nofollow" title="1.6.1">1.6.1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.6.0/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.6.0" rel="nofollow" title="1.6.0">1.6.0</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.5.1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.5.1" rel="nofollow" title="1.5.1">1.5.1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.5.0b2/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.5.0b2" rel="nofollow" title="1.5.0b2">1.5.0b2</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.5.0b1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.5.0b1" rel="nofollow" title="1.5.0b1">1.5.0b1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.5.0/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.5.0" rel="nofollow" title="1.5.0">1.5.0</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.4.4/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.4.4" rel="nofollow" title="1.4.4">1.4.4</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.4.3/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.4.3" rel="nofollow" title="1.4.3">1.4.3</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.4.2/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.4.2" rel="nofollow" title="1.4.2">1.4.2</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.4.1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.4.1" rel="nofollow" title="1.4.1">1.4.1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.4.0/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.4.0" rel="nofollow" title="1.4.0">1.4.0</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.3.1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.3.1" rel="nofollow" title="1.3.1">1.3.1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.3.0/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.3.0" rel="nofollow" title="1.3.0">1.3.0</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.2.1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.2.1" rel="nofollow" title="1.2.1">1.2.1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.2.0/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.2.0" rel="nofollow" title="1.2.0">1.2.0</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.1.2/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.1.2" rel="nofollow" title="1.1.2">1.1.2</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.1.1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.1.1" rel="nofollow" title="1.1.1">1.1.1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.1.0/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.1.0" rel="nofollow" title="1.1.0">1.1.0</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.6/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.6" rel="nofollow" title="1.0.6">1.0.6</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.5/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.5" rel="nofollow" title="1.0.5">1.0.5</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.4/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.4" rel="nofollow" title="1.0.4">1.0.4</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.3/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.3" rel="nofollow" title="1.0.3">1.0.3</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.2/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.2" rel="nofollow" title="1.0.2">1.0.2</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.1/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.1" rel="nofollow" title="1.0.1">1.0.1</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b31/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b31" rel="nofollow" title="1.0.0b31">1.0.0b31</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b30/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b30" rel="nofollow" title="1.0.0b30">1.0.0b30</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b29/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b29" rel="nofollow" title="1.0.0b29">1.0.0b29</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b28/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b28" rel="nofollow" title="1.0.0b28">1.0.0b28</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b26/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b26" rel="nofollow" title="1.0.0b26">1.0.0b26</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b24/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b24" rel="nofollow" title="1.0.0b24">1.0.0b24</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b22/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b22" rel="nofollow" title="1.0.0b22">1.0.0b22</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b19/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b19" rel="nofollow" title="1.0.0b19">1.0.0b19</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b13/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b13" rel="nofollow" title="1.0.0b13">1.0.0b13</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b12/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b12" rel="nofollow" title="1.0.0b12">1.0.0b12</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b11/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b11" rel="nofollow" title="1.0.0b11">1.0.0b11</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b10/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b10" rel="nofollow" title="1.0.0b10">1.0.0b10</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b9/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b9" rel="nofollow" title="1.0.0b9">1.0.0b9</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b8/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b8" rel="nofollow" title="1.0.0b8">1.0.0b8</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0b7/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0b7" rel="nofollow" title="1.0.0b7">1.0.0b7</a>
              </div> <!-- /.select-menu-item -->
              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                <a href="/buildout/buildout/blob/1.0.0/bootstrap/bootstrap.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="1.0.0" rel="nofollow" title="1.0.0">1.0.0</a>
              </div> <!-- /.select-menu-item -->

            <div class="select-menu-no-results js-not-filterable">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/buildout/buildout" class="selected tabnav-tab" highlight="repo_source">Files</a></li>
    <li><a href="/buildout/buildout/commits/master" class="tabnav-tab" highlight="repo_commits">Commits</a></li>
    <li><a href="/buildout/buildout/branches" class="tabnav-tab" highlight="repo_branches" rel="nofollow">Branches <span class="counter ">22</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:d6f50a829205c90a6c09aa6251584b2c -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:d6f50a829205c90a6c09aa6251584b2c -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/buildout/buildout" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">buildout</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/buildout/buildout/tree/master/bootstrap" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">bootstrap</span></a></span><span class="separator"> / </span><strong class="final-path">bootstrap.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="bootstrap/bootstrap.py" data-copied-hint="copied!" title="copy to clipboard"><span class="mini-icon mini-icon-clipboard"></span></span>
        </div>

      <a href="/buildout/buildout/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/701288f165cd8c7d54be97427095ed17?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/rvanlaar" rel="author">rvanlaar</a></span>
    <time class="js-relative-date" datetime="2013-02-16T05:05:30-08:00" title="2013-02-16 05:05:30">February 16, 2013</time>
    <div class="commit-title">
        <a href="/buildout/buildout/commit/ee709cfb00229fbd8fc8554db8ffffdf06a46808" class="message">PEP8 changes for bootstrap.py</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>8</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="jimfulton" href="/buildout/buildout/commits/master/bootstrap/bootstrap.py?author=jimfulton"><img height="20" src="https://secure.gravatar.com/avatar/caacb731f9d4a5850385428ee0a5f954?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="tarekziade" href="/buildout/buildout/commits/master/bootstrap/bootstrap.py?author=tarekziade"><img height="20" src="https://secure.gravatar.com/avatar/b502021b659b0ea548b723e3b73e94d2?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="cjw296" href="/buildout/buildout/commits/master/bootstrap/bootstrap.py?author=cjw296"><img height="20" src="https://secure.gravatar.com/avatar/276928028a2075ceeb0b7aface8e2e2a?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="rvanlaar" href="/buildout/buildout/commits/master/bootstrap/bootstrap.py?author=rvanlaar"><img height="20" src="https://secure.gravatar.com/avatar/701288f165cd8c7d54be97427095ed17?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="hannosch" href="/buildout/buildout/commits/master/bootstrap/bootstrap.py?author=hannosch"><img height="20" src="https://secure.gravatar.com/avatar/442ad68d70ba0e030f167c6aca346975?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="garyposter" href="/buildout/buildout/commits/master/bootstrap/bootstrap.py?author=garyposter"><img height="20" src="https://secure.gravatar.com/avatar/2d3531431d4e729871590238113c6c4b?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="georgyberdyshev" href="/buildout/buildout/commits/master/bootstrap/bootstrap.py?author=georgyberdyshev"><img height="20" src="https://secure.gravatar.com/avatar/e6c4062f5a29be6d31dd0103010f9c44?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="zopyx" href="/buildout/buildout/commits/master/bootstrap/bootstrap.py?author=zopyx"><img height="20" src="https://secure.gravatar.com/avatar/302db24de03cf31217361bff44b3f168?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2>Users on GitHub who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/caacb731f9d4a5850385428ee0a5f954?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/jimfulton">jimfulton</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/b502021b659b0ea548b723e3b73e94d2?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/tarekziade">tarekziade</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/276928028a2075ceeb0b7aface8e2e2a?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/cjw296">cjw296</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/701288f165cd8c7d54be97427095ed17?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/rvanlaar">rvanlaar</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/442ad68d70ba0e030f167c6aca346975?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/hannosch">hannosch</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/2d3531431d4e729871590238113c6c4b?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/garyposter">garyposter</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/e6c4062f5a29be6d31dd0103010f9c44?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/georgyberdyshev">georgyberdyshev</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/302db24de03cf31217361bff44b3f168?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/zopyx">zopyx</a>
        </li>
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/buildout/buildout/blob/bbfa363c836ad16555585c0d82ebc1a2de3c88b4/bootstrap/bootstrap.py" data-title="buildout/bootstrap/bootstrap.py at master · buildout/buildout · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>173 lines (142 sloc)</span>
                <span>5.741 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/buildout/buildout/raw/master/bootstrap/bootstrap.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/buildout/buildout/blame/master/bootstrap/bootstrap.py" class="button minibutton ">Blame</a>
                  <a href="/buildout/buildout/commits/master/bootstrap/bootstrap.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="data type-python js-blob-data">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
</pre>
          </td>
          <td width="100%">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">##############################################################################</span></div><div class='line' id='LC2'><span class="c">#</span></div><div class='line' id='LC3'><span class="c"># Copyright (c) 2006 Zope Foundation and Contributors.</span></div><div class='line' id='LC4'><span class="c"># All Rights Reserved.</span></div><div class='line' id='LC5'><span class="c">#</span></div><div class='line' id='LC6'><span class="c"># This software is subject to the provisions of the Zope Public License,</span></div><div class='line' id='LC7'><span class="c"># Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.</span></div><div class='line' id='LC8'><span class="c"># THIS SOFTWARE IS PROVIDED &quot;AS IS&quot; AND ANY AND ALL EXPRESS OR IMPLIED</span></div><div class='line' id='LC9'><span class="c"># WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED</span></div><div class='line' id='LC10'><span class="c"># WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS</span></div><div class='line' id='LC11'><span class="c"># FOR A PARTICULAR PURPOSE.</span></div><div class='line' id='LC12'><span class="c">#</span></div><div class='line' id='LC13'><span class="c">##############################################################################</span></div><div class='line' id='LC14'><span class="sd">&quot;&quot;&quot;Bootstrap a buildout-based project</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><span class="sd">Simply run this script in a directory containing a buildout.cfg.</span></div><div class='line' id='LC17'><span class="sd">The script accepts buildout command-line options, so you can</span></div><div class='line' id='LC18'><span class="sd">use the -c option to specify an alternate configuration file.</span></div><div class='line' id='LC19'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC22'><span class="kn">import</span> <span class="nn">shutil</span></div><div class='line' id='LC23'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC24'><span class="kn">import</span> <span class="nn">tempfile</span></div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'><span class="kn">from</span> <span class="nn">optparse</span> <span class="kn">import</span> <span class="n">OptionParser</span></div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'><span class="n">tmpeggs</span> <span class="o">=</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">mkdtemp</span><span class="p">()</span></div><div class='line' id='LC29'><br/></div><div class='line' id='LC30'><span class="n">usage</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;</span><span class="se">\</span></div><div class='line' id='LC31'><span class="s">[DESIRED PYTHON FOR BUILDOUT] bootstrap.py [options]</span></div><div class='line' id='LC32'><br/></div><div class='line' id='LC33'><span class="s">Bootstraps a buildout-based project.</span></div><div class='line' id='LC34'><br/></div><div class='line' id='LC35'><span class="s">Simply run this script in a directory containing a buildout.cfg, using the</span></div><div class='line' id='LC36'><span class="s">Python that you want bin/buildout to use.</span></div><div class='line' id='LC37'><br/></div><div class='line' id='LC38'><span class="s">Note that by using --setup-source and --download-base to point to</span></div><div class='line' id='LC39'><span class="s">local resources, you can keep this script from going over the network.</span></div><div class='line' id='LC40'><span class="s">&#39;&#39;&#39;</span></div><div class='line' id='LC41'><br/></div><div class='line' id='LC42'><span class="n">parser</span> <span class="o">=</span> <span class="n">OptionParser</span><span class="p">(</span><span class="n">usage</span><span class="o">=</span><span class="n">usage</span><span class="p">)</span></div><div class='line' id='LC43'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-v&quot;</span><span class="p">,</span> <span class="s">&quot;--version&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;use a specific zc.buildout version&quot;</span><span class="p">)</span></div><div class='line' id='LC44'><br/></div><div class='line' id='LC45'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-t&quot;</span><span class="p">,</span> <span class="s">&quot;--accept-buildout-test-releases&quot;</span><span class="p">,</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest</span><span class="o">=</span><span class="s">&#39;accept_buildout_test_releases&#39;</span><span class="p">,</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">action</span><span class="o">=</span><span class="s">&quot;store_true&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="p">(</span><span class="s">&quot;Normally, if you do not specify a --version, the &quot;</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;bootstrap script and buildout gets the newest &quot;</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;*final* versions of zc.buildout and its recipes and &quot;</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;extensions for you.  If you use this flag, &quot;</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;bootstrap and buildout will get the newest releases &quot;</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;even if they are alphas or betas.&quot;</span><span class="p">))</span></div><div class='line' id='LC54'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-c&quot;</span><span class="p">,</span> <span class="s">&quot;--config-file&quot;</span><span class="p">,</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="p">(</span><span class="s">&quot;Specify the path to the buildout configuration &quot;</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;file to be used.&quot;</span><span class="p">))</span></div><div class='line' id='LC57'><span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-f&quot;</span><span class="p">,</span> <span class="s">&quot;--find-links&quot;</span><span class="p">,</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="p">(</span><span class="s">&quot;Specify a URL to search for buildout releases&quot;</span><span class="p">))</span></div><div class='line' id='LC59'><br/></div><div class='line' id='LC60'><br/></div><div class='line' id='LC61'><span class="n">options</span><span class="p">,</span> <span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span></div><div class='line' id='LC62'><br/></div><div class='line' id='LC63'><span class="c">######################################################################</span></div><div class='line' id='LC64'><span class="c"># load/install distribute</span></div><div class='line' id='LC65'><br/></div><div class='line' id='LC66'><span class="n">to_reload</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC67'><span class="k">try</span><span class="p">:</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">pkg_resources</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">setuptools</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">pkg_resources</span><span class="p">,</span> <span class="s">&#39;_distribute&#39;</span><span class="p">):</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">to_reload</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">ImportError</span></div><div class='line' id='LC73'><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ez</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC75'><br/></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib.request</span> <span class="kn">import</span> <span class="n">urlopen</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">urllib2</span> <span class="kn">import</span> <span class="n">urlopen</span></div><div class='line' id='LC80'><br/></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">exec</span><span class="p">(</span><span class="n">urlopen</span><span class="p">(</span><span class="s">&#39;http://python-distribute.org/distribute_setup.py&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> </div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ez</span><span class="p">)</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">setup_args</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">to_dir</span><span class="o">=</span><span class="n">tmpeggs</span><span class="p">,</span> <span class="n">download_delay</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">no_fake</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ez</span><span class="p">[</span><span class="s">&#39;use_setuptools&#39;</span><span class="p">](</span><span class="o">**</span><span class="n">setup_args</span><span class="p">)</span></div><div class='line' id='LC85'><br/></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">to_reload</span><span class="p">:</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">reload</span><span class="p">(</span><span class="n">pkg_resources</span><span class="p">)</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">pkg_resources</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># This does not (always?) update the default working set.  We will</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># do it.</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="p">:</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">path</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">pkg_resources</span><span class="o">.</span><span class="n">working_set</span><span class="o">.</span><span class="n">entries</span><span class="p">:</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pkg_resources</span><span class="o">.</span><span class="n">working_set</span><span class="o">.</span><span class="n">add_entry</span><span class="p">(</span><span class="n">path</span><span class="p">)</span></div><div class='line' id='LC94'><br/></div><div class='line' id='LC95'><span class="c">######################################################################</span></div><div class='line' id='LC96'><span class="c"># Install buildout</span></div><div class='line' id='LC97'><br/></div><div class='line' id='LC98'><span class="n">ws</span> <span class="o">=</span> <span class="n">pkg_resources</span><span class="o">.</span><span class="n">working_set</span></div><div class='line' id='LC99'><br/></div><div class='line' id='LC100'><span class="n">cmd</span> <span class="o">=</span> <span class="p">[</span><span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">,</span> <span class="s">&#39;-c&#39;</span><span class="p">,</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;from setuptools.command.easy_install import main; main()&#39;</span><span class="p">,</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;-mZqNxd&#39;</span><span class="p">,</span> <span class="n">tmpeggs</span><span class="p">]</span></div><div class='line' id='LC103'><br/></div><div class='line' id='LC104'><span class="n">find_links</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;bootstrap-testing-find-links&#39;</span><span class="p">,</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">options</span><span class="o">.</span><span class="n">find_links</span> <span class="ow">or</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;http://downloads.buildout.org/&#39;</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">accept_buildout_test_releases</span> <span class="k">else</span> <span class="bp">None</span><span class="p">)</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC110'><span class="k">if</span> <span class="n">find_links</span><span class="p">:</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cmd</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="s">&#39;-f&#39;</span><span class="p">,</span> <span class="n">find_links</span><span class="p">])</span></div><div class='line' id='LC112'><br/></div><div class='line' id='LC113'><span class="n">distribute_path</span> <span class="o">=</span> <span class="n">ws</span><span class="o">.</span><span class="n">find</span><span class="p">(</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pkg_resources</span><span class="o">.</span><span class="n">Requirement</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="s">&#39;distribute&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">location</span></div><div class='line' id='LC115'><br/></div><div class='line' id='LC116'><span class="n">requirement</span> <span class="o">=</span> <span class="s">&#39;zc.buildout&#39;</span></div><div class='line' id='LC117'><span class="n">version</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">version</span></div><div class='line' id='LC118'><span class="k">if</span> <span class="n">version</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">options</span><span class="o">.</span><span class="n">accept_buildout_test_releases</span><span class="p">:</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Figure out the most recent final version of zc.buildout.</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">setuptools.package_index</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_final_parts</span> <span class="o">=</span> <span class="s">&#39;*final-&#39;</span><span class="p">,</span> <span class="s">&#39;*final&#39;</span></div><div class='line' id='LC122'><br/></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_final_version</span><span class="p">(</span><span class="n">parsed_version</span><span class="p">):</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">parsed_version</span><span class="p">:</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">part</span><span class="p">[:</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;*&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">part</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">_final_parts</span><span class="p">):</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">index</span> <span class="o">=</span> <span class="n">setuptools</span><span class="o">.</span><span class="n">package_index</span><span class="o">.</span><span class="n">PackageIndex</span><span class="p">(</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">search_path</span><span class="o">=</span><span class="p">[</span><span class="n">distribute_path</span><span class="p">])</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">find_links</span><span class="p">:</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">index</span><span class="o">.</span><span class="n">add_find_links</span><span class="p">((</span><span class="n">find_links</span><span class="p">,))</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span> <span class="o">=</span> <span class="n">pkg_resources</span><span class="o">.</span><span class="n">Requirement</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">requirement</span><span class="p">)</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">index</span><span class="o">.</span><span class="n">obtain</span><span class="p">(</span><span class="n">req</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">best</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bestv</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">dist</span> <span class="ow">in</span> <span class="n">index</span><span class="p">[</span><span class="n">req</span><span class="o">.</span><span class="n">project_name</span><span class="p">]:</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">distv</span> <span class="o">=</span> <span class="n">dist</span><span class="o">.</span><span class="n">parsed_version</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">_final_version</span><span class="p">(</span><span class="n">distv</span><span class="p">):</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">bestv</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">distv</span> <span class="o">&gt;</span> <span class="n">bestv</span><span class="p">:</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">best</span> <span class="o">=</span> <span class="p">[</span><span class="n">dist</span><span class="p">]</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bestv</span> <span class="o">=</span> <span class="n">distv</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">distv</span> <span class="o">==</span> <span class="n">bestv</span><span class="p">:</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">best</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dist</span><span class="p">)</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">best</span><span class="p">:</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">best</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version</span> <span class="o">=</span> <span class="n">best</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">version</span></div><div class='line' id='LC147'><span class="k">if</span> <span class="n">version</span><span class="p">:</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">requirement</span> <span class="o">=</span> <span class="s">&#39;==&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">((</span><span class="n">requirement</span><span class="p">,</span> <span class="n">version</span><span class="p">))</span></div><div class='line' id='LC149'><span class="n">cmd</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">requirement</span><span class="p">)</span></div><div class='line' id='LC150'><br/></div><div class='line' id='LC151'><span class="kn">import</span> <span class="nn">subprocess</span></div><div class='line' id='LC152'><span class="k">if</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">call</span><span class="p">(</span><span class="n">cmd</span><span class="p">,</span> <span class="n">env</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">,</span> <span class="n">PYTHONPATH</span><span class="o">=</span><span class="n">distribute_path</span><span class="p">))</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;Failed to execute command:</span><span class="se">\n</span><span class="si">%s</span><span class="s">&quot;</span><span class="p">,</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">repr</span><span class="p">(</span><span class="n">cmd</span><span class="p">)[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC156'><br/></div><div class='line' id='LC157'><span class="c">######################################################################</span></div><div class='line' id='LC158'><span class="c"># Import and run buildout</span></div><div class='line' id='LC159'><br/></div><div class='line' id='LC160'><span class="n">ws</span><span class="o">.</span><span class="n">add_entry</span><span class="p">(</span><span class="n">tmpeggs</span><span class="p">)</span></div><div class='line' id='LC161'><span class="n">ws</span><span class="o">.</span><span class="n">require</span><span class="p">(</span><span class="n">requirement</span><span class="p">)</span></div><div class='line' id='LC162'><span class="kn">import</span> <span class="nn">zc.buildout.buildout</span></div><div class='line' id='LC163'><br/></div><div class='line' id='LC164'><span class="k">if</span> <span class="ow">not</span> <span class="p">[</span><span class="n">a</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">args</span> <span class="k">if</span> <span class="s">&#39;=&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">a</span><span class="p">]:</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">args</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;bootstrap&#39;</span><span class="p">)</span></div><div class='line' id='LC166'><br/></div><div class='line' id='LC167'><span class="c"># if -c was provided, we push it back into args for buildout&#39; main function</span></div><div class='line' id='LC168'><span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">config_file</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;-c&#39;</span><span class="p">,</span> <span class="n">options</span><span class="o">.</span><span class="n">config_file</span><span class="p">]</span></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'><span class="n">zc</span><span class="o">.</span><span class="n">buildout</span><span class="o">.</span><span class="n">buildout</span><span class="o">.</span><span class="n">main</span><span class="p">(</span><span class="n">args</span><span class="p">)</span></div><div class='line' id='LC172'><span class="n">shutil</span><span class="o">.</span><span class="n">rmtree</span><span class="p">(</span><span class="n">tmpeggs</span><span class="p">)</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1360648843" height="64" width="64">
</div>


        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.05174s from fe3.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/buildout/buildout/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-icon mega-icon-normalscreen"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="mini-icon mini-icon-brightness"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.05211' data-host='fe3'></span>
    
  </body>
</html>

