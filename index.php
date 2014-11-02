<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="">
  <meta name="author" content="">
  <link rel="icon" href="favicon.ico">

  <title>CTF@HSO Backend</title>

  <!-- Bootstrap core CSS -->
  <link href="css/bootstrap/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/custom/style.css" rel="stylesheet">

  <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
  <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
  <!--<script src="js/debug/ie-emulation-modes-warning.js"></script>-->

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

    <div class="container background center">
      <pre><?php include('background.php'); ?></pre>
    </div>


    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">

      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand disableme" href="#">CTF@HSO</a>
        </div>

        <!-- menu -->
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">

            <li class="active"><a href="sites/home.php" target="#dyncontent">Home</a></li>
            <li><a href="sites/test.php" target="#dyncontent">About</a></li>
            <li><a href="#contact">Contact</a></li>

            <li class="dropdown">
              <a href="" class="dropdown-toggle disableme" data-toggle="dropdown">Dropdown<span class="caret"></span></a>
              <ul class="dropdown-menu" role="menu">
                <li><a href="sites/test.php" target="#dyncontent">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Nav header</li>
                <li><a href="#">Separated link</a></li>
                <li><a href="#">One more separated link</a></li>
              </ul>
            </li>
          </ul>

          <form class="navbar-form navbar-right" role="form">
            <div class="form-group">
              <input type="text" placeholder="Email" class="form-control input">
            </div>
            <div class="form-group">
              <input type="password" placeholder="Password" class="form-control input">
            </div>
            <div class="btn-group">
              <button type="submit" class="btn btn-success first-child" name="signin">Sign In</button>
              <div class="btn-group-vertical last-child btn-group-2-right">
                <button type="submit" class="btn btn-info first-child" name="register">Sign Up</button>
                <button type="submit" class="btn btn-danger last-child" name="forgotpw">Reset PW</button>
              </div>
            </div>
          </form>


        </div><!--/.nav-collapse -->


      </div>
    </div>



    <div id="dyncontent" class="container">

      <?php include('sites/home.php'); ?>

    </div><!-- /.container -->





<!-- Bootstrap core JavaScript
  ================================================== -->
  <!-- Placed at the end of the document so the pages load faster -->
  <script src="js/jquery/jquery-1.11.1.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  <script src="js/workarounds/ie10-viewport-bug-workaround.js"></script>

<!-- Custom JavaScript -->
  <script src="js/custom.js"></script>


</body>
</html>

