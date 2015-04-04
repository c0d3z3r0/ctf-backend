<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="CTF@HSO Backend">
  <meta name="author" content="Michael Niewöhner">
  <link rel="icon" href="favicon.ico">

  <title>CTF@HSO Backend</title>

  <link href="css/bootstrap.min.css" rel="stylesheet">
  <link href="css/custom/style.css" rel="stylesheet">
  <link href="css/c3.min.css" rel="stylesheet">



  <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
  <!--[if lt IE 9]>
    <script src="js/html5shiv.min.js"></script>
    <script src="js/respond.min.js"></script>
    <![endif]-->

  </head>


  <body>

    <noscript>
      <div id="nojs-banner" class="container">
        <div class="content home-content">
          <h1>Welcome to CTF@HSO.</h1>
          <p class="lead">You need to enable JavaScript to use the backend.<br>Firefox and Chrome are recommended.</p>
        </div>
      </div>
    </noscript>

    <div class="container background">
      <pre><?php include('background.php'); ?></pre>
    </div>


    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">

      <div class="container-fluid">
        <div class="navbar-header">
          <span class="navbar-brand">CTF@HSO</span>
        </div>

        <!-- menu -->
        <div class="navbar-left">
          <ul class="nav navbar-nav">

            <li class="outside active"><a href="sites/home.php" target="#dyncontent">Home</a></li>
            <li class="inside hidden"><a href="sites/flag.php" target="#dyncontent">Submit Flag</a></li>
            <li class=""><a href="sites/scores.php" target="#dyncontent">Scoreboard</a></li>
            <li class="hidden"><a href="sites/stats.php" target="#dyncontent">Statistics</a></li>
            <li class="inside hidden"><a href="sites/stats.php" target="#dyncontent">Challenges</a></li>
            <li class="inside hidden"><a href="sites/stats.php" target="#dyncontent">Hints</a></li>
            <li class="inside hidden"><a href="sites/stats.php" target="#dyncontent">Ticket Manager</a></li>

          </ul>
        </div> <!-- /menu -->

        <div class="navbar-right">

          <form id="loginform" class="navbar-form hidden" role="form" >
            <div id="loginfields" class="form-group">
              <div class="form-group form-group-sm">
                <input type="text" placeholder="User or E-Mail" class="form-control input">
                <input type="password" placeholder="Password" class="form-control input">
              </div>
            </div>
            <div class="btn-group btn-group-sm">
              <button id="signin" type="submit" class="btn btn-sm btn-success first-child" name="signin">Sign In</button>
              <div id="registerbtns" class="btn-group-sm btn-group-vertical last-child btn-group-2-right">
                <button type="submit" class="btn btn-info btn-sm first-child" name="register">Sign Up</button>
                <button type="submit" class="btn btn-danger btn-sm last-child" name="forgotpw">Reset PW</button>
              </div>
            </div>
          </form>


          <!-- profile -->
          <ul id="profile" class="nav navbar-nav">
            <li class="dropdown">
              <a class="dropdown-toggle" data-toggle="dropdown">
                <span class="glyphicon glyphicon-user"></span> <span class="caret"></span>
              </a>

              <ul class="dropdown-menu" role="menu">
                <li class="dropdown-header">c0d3z3r0</li>
                <li><a href="sites/test.php" target="#dyncontent">User Settings</a></li>
                <li class="divider"></li>

                <!-- Admin menu - only visible for admins -->
                <li class="dropdown-header">Administration</li>
                <li class=""><a href="sites/test.php" target="#dyncontent">General Settings</a></li>
                <li class=""><a href="sites/test.php" target="#dyncontent">Users</a></li>
                <li class=""><a href="sites/test.php" target="#dyncontent">Challenges</a></li>
                <li class=""><a href="sites/test.php" target="#dyncontent">Hints</a></li>
                <li class=""><a href="sites/test.php" target="#dyncontent">Ticket Manager</a></li>
                <li class="divider"></li>
                <!-- / admin menu -->

                <li><a href="sites/test.php" target="#dyncontent">Logout</a></li>
              </ul>
            </li>
          </ul> <!-- /profile -->

        </div> <!-- /navbar-right -->
      </div> <!-- /container-fluid -->
    </div> <!-- /navbar -->



    <!-- dyncontent -->
    <div id="dyncontent" class="container">

      <?php include('sites/submit_flag.php'); ?>

    </div><!-- /dyncontent -->



    <!-- JavaScript -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/d3.min.js"></script>
    <script src="js/c3.min.js"></script>

    <!-- Custom JavaScript -->
    <script src="js/custom.js"></script>


  </body>
  </html>

