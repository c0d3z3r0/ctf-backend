<div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
  <div class="container-fluid">
    <div class="navbar-header">
      <span class="navbar-brand">CTF@HSO</span>
    </div>

    <!-- menu -->
    <div class="navbar-left">
      <ul class="nav navbar-nav">
        <li class="outside active"> <a href="{{ url('content/home') }}" target="#dyncontent">Home</a></li>
        <li class="inside hidden"> <a href="{{ url('content/submit_flag') }}" target="#dyncontent">Submit Flag</a></li>
        <li class=""> <a href="{{ url('content/scores') }}" target="#dyncontent">Scoreboard</a></li>
        <li class="hidden"> <a href="{{ url('content/stats') }}" target="#dyncontent">Statistics</a></li>
        <li class="inside hidden"> <a href="{{ url('content/stats') }}" target="#dyncontent">Challenges</a></li>
        <li class="inside hidden"> <a href="{{ url('content/stats') }}" target="#dyncontent">Hints</a></li>
        <li class="inside hidden"> <a href="{{ url('content/test') }}" target="#dyncontent">Ticket Manager</a></li>
      </ul>
    </div>

    <!-- /menu -->
    <div class="navbar-right">
      <form id="loginform" class="navbar-form hidden" role="form">
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
            <span class="glyphicon glyphicon-user"></span>
            <span class="caret"></span>
          </a>

          <ul class="dropdown-menu" role="menu">
            <li class="dropdown-header">c0d3z3r0</li>
            <li><a href="{{ url('content/stats') }}" target="#dyncontent">User Settings</a></li>
            <li class="divider"></li>

            <!-- Admin menu - only visible for admins -->
            <li class="dropdown-header">Administration</li>
            <li class=""><a href="{{ url('content/test') }}" target="#dyncontent">General Settings</a></li>
            <li class=""><a href="{{ url('content/test') }}" target="#dyncontent">Users</a></li>
            <li class=""><a href="{{ url('content/test') }}" target="#dyncontent">Challenges</a></li>
            <li class=""><a href="{{ url('content/test') }}" target="#dyncontent">Hints</a></li>
            <li class=""><a href="{{ url('content/test') }}" target="#dyncontent">Ticket Manager</a></li>
            <li class="divider"></li>
            <!-- / admin menu -->

            <li><a href="{{ url('content/test') }}" target="#dyncontent">Logout</a></li>
          </ul>
        </li>
      </ul>
      <!-- /profile -->

    </div>
    <!-- /navbar-right -->

  </div>
  <!-- /container-fluid -->

</div>
<!-- /navbar -->