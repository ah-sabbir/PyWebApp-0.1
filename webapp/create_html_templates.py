template = """<!DOCTYPE html>
<html lang="en">
<title>my template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="{0}">
<body>

<!-- Navbar -->
<div class="Header">
  <div class="first_nav_menu">
    <a class="primaryMenu" href="ToggleNav" title="Toggle Navigation Menu"><i class="None"></i></a>
    <a href="#" class="HomeNavMenu">HOME</a>
    <div class="smallDropDownClass">
      <button class="moreButton" title="More">MORE <i class="fa fa-caret-down"></i></button>     
      <div class="w3-dropdown-content w3-bar-block w3-card-4">
        <a href="#" class="Menus">Merchandise</a>
      </div>
    </div>
    <a href="hide button" class="hideButtonClass"><i class="fa fa-search"></i></a>
  </div>
</div>

<!-- Navbar on small screens (remove the onclick attribute if you want the navbar to always show on top of the content when clicking on the links) -->
<div id="navDemo" class="navClass" style="margin-top:46px">
  <a href="#menu" class="">menu</a>
</div>

<!-- Page content -->
<div class="w3-content" style="max-width:2000px;margin-top:46px">

  <!-- Automatic Slideshow Images -->
  <div class="mySlides w3-display-container w3-center">
    <img src="/w3images/la.jpg" style="width:100%">
    <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
      <h3>Los Angeles</h3>
      <p><b>We had the best time playing at Venice Beach!</b></p>   
    </div>
  </div>
  <div class="mySlides w3-display-container w3-center">
    <img src="/w3images/ny.jpg" style="width:100%">
    <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
      <h3>New York</h3>
      <p><b>The atmosphere in New York is lorem ipsum.</b></p>    
    </div>
  </div>
  <div class="mySlides w3-display-container w3-center">
    <img src="/w3images/chicago.jpg" style="width:100%">
    <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
      <h3>Chicago</h3>
      <p><b>Thank you, Chicago - A night we won't forget.</b></p>    
    </div>
  </div>

  <!-- The Band Section -->
  <div class="w3-container w3-content w3-center w3-padding-64" style="max-width:800px" id="band">
    <h2 class="w3-wide">THE BAND</h2>
    <p class="w3-opacity"><i>We love music</i></p>
    <p class="w3-justify">We have created a fictional band website. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
      ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum consectetur
      adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    <div class="w3-row w3-padding-32">
      <div class="w3-third">
        <p>Name</p>
        <img src="/w3images/bandmember.jpg" class="w3-round w3-margin-bottom" alt="Random Name" style="width:60%">
      </div>
      <div class="w3-third">
        <p>Name</p>
        <img src="/w3images/bandmember.jpg" class="w3-round w3-margin-bottom" alt="Random Name" style="width:60%">
      </div>
      <div class="w3-third">
        <p>Name</p>
        <img src="/w3images/bandmember.jpg" class="w3-round" alt="Random Name" style="width:60%">
      </div>
    </div>
  </div>

  <!-- The Tour Section -->
<div>
    <!-- this is the tour section -->
    <h4> Tour section</h4>
</div>

  <!-- The Contact Section -->
  <div class="w3-container w3-content w3-padding-64" style="max-width:800px" id="contact">
    <h2 class="w3-wide w3-center">CONTACT</h2>
    <p class="w3-opacity w3-center"><i>Fan? Drop a note!</i></p>
    <div class="w3-row w3-padding-32">
      <div class="w3-col m6 w3-large w3-margin-bottom">
        <i class="fa fa-map-marker" style="width:30px"></i> Chicago, US<br>
        <i class="fa fa-phone" style="width:30px"></i> Phone: +00 151515<br>
        <i class="fa fa-envelope" style="width:30px"> </i> Email: mail@mail.com<br>
      </div>
      <div class="w3-col m6">
        <form action="/action_page.php" target="_blank">
          <div class="w3-row-padding" style="margin:0 -16px 8px -16px">
            <div class="w3-half">
              <input class="w3-input w3-border" type="text" placeholder="Name" required name="Name">
            </div>
            <div class="w3-half">
              <input class="w3-input w3-border" type="text" placeholder="Email" required name="Email">
            </div>
          </div>
          <input class="w3-input w3-border" type="text" placeholder="Message" required name="Message">
          <button class="w3-button w3-black w3-section w3-right" type="submit">SEND</button>
        </form>
      </div>
    </div>
  </div>
  
<!-- End Page Content -->
</div>

<!-- Image of location/map -->
<img src="/w3images/map.jpg" class="w3-image w3-greyscale-min" style="width:100%">

<!-- Footer -->
<footer class="w3-container w3-padding-64 w3-center w3-opacity w3-light-grey w3-xlarge">
<!-- #####################  this is Footer Section -->
</footer>

<script src="{1}">

</script>

</body>
</html>
"""

def template_maker(css_files,js_files=None):
    template = """<!DOCTYPE html>
    <html lang="en">
    <title>my template</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{0}">
    <body>

    <!-- Navbar -->
    <div class="Header">
      <div class="first_nav_menu">
        <a class="primaryMenu" href="ToggleNav" title="Toggle Navigation Menu"><i class="None"></i></a>
        <a href="#" class="HomeNavMenu">HOME</a>
        <div class="smallDropDownClass">
          <button class="moreButton" title="More">MORE <i class="fa fa-caret-down"></i></button>     
          <div class="w3-dropdown-content w3-bar-block w3-card-4">
            <a href="#" class="Menus">Merchandise</a>
          </div>
        </div>
        <a href="hide button" class="hideButtonClass"><i class="fa fa-search"></i></a>
      </div>
    </div>

    <!-- Navbar on small screens (remove the onclick attribute if you want the navbar to always show on top of the content when clicking on the links) -->
    <div id="navDemo" class="navClass" style="margin-top:46px">
      <a href="#menu" class="">menu</a>
    </div>

    <!-- Page content -->
    <div class="w3-content" style="max-width:2000px;margin-top:46px">

      <!-- Automatic Slideshow Images -->
      <div class="mySlides w3-display-container w3-center">
        <img src="/w3images/la.jpg" style="width:100%">
        <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
          <h3>Los Angeles</h3>
          <p><b>We had the best time playing at Venice Beach!</b></p>   
        </div>
      </div>
      <div class="mySlides w3-display-container w3-center">
        <img src="/w3images/ny.jpg" style="width:100%">
        <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
          <h3>New York</h3>
          <p><b>The atmosphere in New York is lorem ipsum.</b></p>    
        </div>
      </div>
      <div class="mySlides w3-display-container w3-center">
        <img src="/w3images/chicago.jpg" style="width:100%">
        <div class="w3-display-bottommiddle w3-container w3-text-white w3-padding-32 w3-hide-small">
          <h3>Chicago</h3>
          <p><b>Thank you, Chicago - A night we won't forget.</b></p>    
        </div>
      </div>

      <!-- The Band Section -->
      <div class="w3-container w3-content w3-center w3-padding-64" style="max-width:800px" id="band">
        <h2 class="w3-wide">THE BAND</h2>
        <p class="w3-opacity"><i>We love music</i></p>
        <p class="w3-justify">We have created a fictional band website. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
          ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum consectetur
          adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        <div class="w3-row w3-padding-32">
          <div class="w3-third">
            <p>Name</p>
            <img src="/w3images/bandmember.jpg" class="w3-round w3-margin-bottom" alt="Random Name" style="width:60%">
          </div>
          <div class="w3-third">
            <p>Name</p>
            <img src="/w3images/bandmember.jpg" class="w3-round w3-margin-bottom" alt="Random Name" style="width:60%">
          </div>
          <div class="w3-third">
            <p>Name</p>
            <img src="/w3images/bandmember.jpg" class="w3-round" alt="Random Name" style="width:60%">
          </div>
        </div>
      </div>

      <!-- The Tour Section -->
    <div>
        <!-- this is the tour section -->
        <h4> Tour section</h4>
    </div>

      <!-- The Contact Section -->
      <div class="w3-container w3-content w3-padding-64" style="max-width:800px" id="contact">
        <h2 class="w3-wide w3-center">CONTACT</h2>
        <p class="w3-opacity w3-center"><i>Fan? Drop a note!</i></p>
        <div class="w3-row w3-padding-32">
          <div class="w3-col m6 w3-large w3-margin-bottom">
            <i class="fa fa-map-marker" style="width:30px"></i> Chicago, US<br>
            <i class="fa fa-phone" style="width:30px"></i> Phone: +00 151515<br>
            <i class="fa fa-envelope" style="width:30px"> </i> Email: mail@mail.com<br>
          </div>
          <div class="w3-col m6">
            <form action="/action_page.php" target="_blank">
              <div class="w3-row-padding" style="margin:0 -16px 8px -16px">
                <div class="w3-half">
                  <input class="w3-input w3-border" type="text" placeholder="Name" required name="Name">
                </div>
                <div class="w3-half">
                  <input class="w3-input w3-border" type="text" placeholder="Email" required name="Email">
                </div>
              </div>
              <input class="w3-input w3-border" type="text" placeholder="Message" required name="Message">
              <button class="w3-button w3-black w3-section w3-right" type="submit">SEND</button>
            </form>
          </div>
        </div>
      </div>
      
    <!-- End Page Content -->
    </div>

    <!-- Image of location/map -->
    <img src="/w3images/map.jpg" class="w3-image w3-greyscale-min" style="width:100%">

    <!-- Footer -->
    <footer class="w3-container w3-padding-64 w3-center w3-opacity w3-light-grey w3-xlarge">
    <!-- #####################  this is Footer Section -->
    </footer>

    <script src="{1}">

    </script>

    </body>
    </html>
    """.format(cssfiles,jsfiles)

import sys,os
from os import system
filename = sys.argv
txt = ""
for i in filename[1:]:
    print(i)
    if ".html" in i:
        try:
            os.makedirs("Templates")
        except Exception as e:
            print(e)
        with open("Templates/"+i,"w+") as writer:
            writer.write(template)
    elif ".css" in i:
        try:
            os.makedirs("static/css")
        except Exception as e:
            print(e)
        with open("static/css/"+i,"w+") as r:
            r.write('body {font-family: "Lato", sans-serif}')
    elif ".js" in i:
        try:
            os.makedirs("static/js")
        except Exception as e:
            print(e)
        with open("static/js/"+i,"w+") as r:
            pass
    else:
        print("you have enter wrong keywords :(")
        






