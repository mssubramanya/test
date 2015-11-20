home_page = '''<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
	<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
</head>
<body lang=EN-US style='tab-interval:.5in'>
<div class=WordSection1>
<p class=MsoNormal><o:p>&nbsp;</o:p></p>
<p class=MsoNormal><o:p>&nbsp;</o:p></p>
<p class=MsoNormal><o:p>&nbsp;</o:p></p>
<p class=MsoNormal><o:p>&nbsp;</o:p></p>
<p class=MsoNormal><o:p>&nbsp;</o:p></p>
<p class=MsoNormal><span style='mso-tab-count:3'>                                                
</span>Please enter your User Name and Password to login:</p>
									<form id="home" action="loginstat" method="post">
<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0in 5.4pt 0in 5.4pt'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:44.5pt'>
  <td width=319 valign=top style='width:239.4pt;border:solid windowtext 1.0pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:44.5pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'>User Name:</p>
  </td>
  <td width=319 valign=top style='width:239.4pt;border:solid windowtext 1.0pt;
  border-left:none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:
  solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:44.5pt'>
  <input type="text" name="username" value="">
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;mso-yfti-lastrow:yes;height:40.0pt'>
  <td width=319 valign=top style='width:239.4pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:40.0pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'>Password :</p>
  </td>
  <td width=319 valign=top style='width:239.4pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:40.0pt'>
  <input type="password" name="password" value="">
  </td>
  </tr>
</table>
<button name="form.submitted" value="Log In" class="btn btn-default"> Log In</button>
<script>
    $(home).ajax({
                 type: "POST",
                 url: "tryjson",
                 data: {username:username},{password:password}
                 cache: false,
            });
    </script>
</form>

<p class=MsoNormal></p>

</div>

</body>

</html>

'''



Login_successful = '''<html xmlns:v="urn:schemas-microsoft-com:vml"
<head>
<meta http-equiv=Content-Type content="text/html; charset=us-ascii">
</head>

<body lang=EN-US style='tab-interval:.5in'>

<div class=WordSection1>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto'><o:p>&nbsp;</o:p></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto'><span
style='mso-tab-count:5'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></p>

<span style='mso-tab-count:15'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>
<span style='mso-tab-count:8'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span
style='mso-spacerun:yes'>&nbsp;</span>

<form id="topcorner" action="logout" method="post">
	<button name="form.logout" value="Log Out" class="btn btn-default">Log Out</button></p>
</form>
<div>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0in 5.4pt 0in 5.4pt'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes'>
  <td width=319 valign=top style='width:239.4pt;border:solid windowtext 1.0pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
  background:#E5B8B7;mso-background-themecolor:accent2;mso-background-themetint:102'>Mongo DB status</p>
  </td>
  <td width=319 valign=top style='width:239.4pt;border:solid windowtext 1.0pt;
  border-left:none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:
  solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto'>{2}</p>
  </td>
 </tr>
</table>
<table class=MsoNormalTable border=1 cellspacing=0 cellpadding=0 width=659
 style='width:494.5pt;border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0in 5.4pt 0in 5.4pt'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:30.1pt'>
  <td width=209 valign=top style='width:157.1pt;border:solid windowtext 1.0pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:30.1pt'>
  <p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
  background:#E5B8B7;'>Sort Users by :</p>
  <form id="sortuser", action="sortusers" method="post">
	<input type="text" name="sortcriteria" value="">
	<button name="form.sortusers" value="Sort By" class="btn btn-default">Find Users By City</button>
  </form>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;mso-yfti-lastrow:yes;height:22.9pt'>
  <td width=659 colspan=2 valign=top style='width:494.5pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt;height:22.9pt'>
  {1}
  </td>
 </tr>
</table>
<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
background:#E5B8B7;><o:p>&nbsp;</o:p></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
background:#E5B8B7;><o:p>&nbsp;</o:p></p>

</div>

<table class=MsoNormalTable border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0in 5.4pt 0in 5.4pt'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes'>
  <td width=209 valign=top style='width:157.1pt;border:solid windowtext 1.0pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
  background:#E5B8B7;'>List of Files of the Directory:</p>
  </td>
  <td width=414 valign=top style='width:310.55pt;border:solid windowtext 1.0pt;
  border-left:none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:
  solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
  background:#E5B8B7;mso-background-themecolor:accent2;mso-background-themetint:
  102'>
  <form id="listdirs", action="listdir" method="post">
	<input type="text" name="Directory" value="C:\\"></p>
	<button name="form.listdir" value="List" class="btn btn-default">List Contents</button>
  </form>
  </td>
 </tr>
</table>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
background:#E5B8B7;mso-background-themecolor:accent2;mso-background-themetint:
102'>
</p>
<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
background:#E5B8B7;mso-background-themecolor:accent2;mso-background-themetint:
102'><o:p>&nbsp;</o:p></p>
</div>
</body>
</html>
'''

sorted_users = '''<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">
<head>
<meta http-equiv=Content-Type content="text/html; charset=us-ascii">
</head>
<body lang=EN-US style='tab-interval:.5in'>
<div class=WordSection1>
<table>
  {0}
 </table>
</div>
</body>
</html>
'''
directory_listing = '''<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">
<head>
<meta http-equiv=Content-Type content="text/html; charset=us-ascii">
</head>
<body lang=EN-US style='tab-interval:.5in'>
<div class=WordSection1>
<table>
  {0}
 </table>
</div>
</body>
</html>
'''
one_user = '''<tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes'>
  <td width=638 valign=top style='width:6.65in;border:solid windowtext 1.0pt;
  mso-border-alt:solid windowtext .5pt;background:#E5B8B7;mso-background-themecolor:
  accent2;mso-background-themetint:102;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
  normal'>{0}</p>
  </td>
 </tr>'''
one_file_folder = '''<tr>
<td width=641 valign=top style='width:481.05pt;border:solid windowtext 1.0pt;
  mso-border-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt;height:21.3pt'>
  <p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
  background:#E5B8B7;mso-background-themecolor:accent2;mso-background-themetint:
  102'>{0}</p>
</td>
</tr>'''
Logout = '''<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
</head>
<body lang=EN-US style='tab-interval:.5in'>
<div class=WordSection1>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'>You have been logged out.<o:p></o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
</div>
</body>
</html>
'''
Login_Failed = '''<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
</head>
<body lang=EN-US style='tab-interval:.5in'>
<div class=WordSection1>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><o:p>&nbsp;</o:p></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'>Login failed. Please check password and username.<o:p></o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
<p class=MsoNormal style='background:#E5B8B7;mso-background-themecolor:accent2;
mso-background-themetint:102'><span style='font-size:14.0pt;line-height:115%'><o:p>&nbsp;</o:p></span></p>
</div>
</body>
</html>
'''
