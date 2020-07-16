import webapp2
import sys
sys.path.insert(0, 'libs')
from bs4 import BeautifulSoup
import requests
import urllib2
from google.appengine.ext import db


class App(db.Model):
    app_img = db.StringProperty(required=True)
    app_name = db.StringProperty(required=True)
    app_package = db.StringProperty(required=True)
# url = "https://play.google.com/store/apps/top?hl=en_IN"
# html_content = requests.get(url).text


# def App_key(app_package=None):
#   return db.Key.from_path('App', app_package)

response = urllib2.urlopen('https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU&hl=en_IN')
html_content = response.read()
soup = BeautifulSoup(html_content, "lxml")
top_free_apps = soup.find_all(attrs = { "class" : "ImZGtf mpg5gc"})
for i in top_free_apps:
    img = i.find_all("img")
    name = i.find_all(attrs={"class": "KoLSrc"})
    package = i.find_all(attrs={"class": "poRVub"})
    obj = App(app_img = img[0]["data-src"], app_name = name[0].text, app_package = package[0]["href"][23:])
    obj.put()
    # print(app_img[0]["data-src"])
    # print(app_name[0].text)
	
	
class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
<!doctype html>
<html>
<head>
        <meta charset="utf-8">
	<style>
	body{
	background-image: url("https://i.pinimg.com/originals/2f/3c/dc/2f3cdc6a9b182457f81b4f72efd26ab3.jpg"); 
}
#a {
	float: right;
	margin-right: 20px;
	margin-top: 30px;
}
#b{
	height: 80px;
	margin-top: 0px;
	border-color: darkblue;
	padding-left: 50px;
	padding-top:20px;
	padding-bottom: 0px;
	background-color:  #00001a;
	/*box-shadow: 10px 10px black;*/
	border-radius: 25px; 
}
#c{
	color:#b1cdcd;
	text-align: center;
	font-size: 40px;
	font-weight: bold;
	margin-top: 10px;
	padding-top: 0px;
	text-shadow: 2px 2px 4px #000000;
}
#d{
	margin-left: 90px;
	color:#507c7c;
	font-size: 30px;
	padding-left: 50px;
}
#e{
	margin-left: 90px;
	color:#507c7c;
	font-size: 30px;
	padding-left: 50px;
}
#f{
	margin-left: 90px;
	color:#507c7c;
	font-size: 30px;
	padding-left: 50px;
}
#app1{
	margin-left: 200px;
	margin-right: 200px;
	float:right;
	text-align:top;
	border-width:2px;
	border-color:red;
	height:150px;
	width : 150px;
	color : white;
	text-align: center;
}
#app2{
	margin-left: 200px;
	float:right;
	text-align:top;
	border-width:2px;
	border-color:red;
	height:150px;
	width : 150px;
	color : white;
	text-align: center;
}
#app3{
	float:right;
	text-align:top;
	border-width:2px;
	border-color:red;
	height:150px;
	width : 150px;
	color : white;
	text-align: center;
}
#app1_img{
	border-radius: 20%;
}
#app2_img{
	border-radius: 20%;
}
#app3_img{
	border-radius: 20%;
}
</style>
	<title>WebApp</title>
</head>
<body>
	<h1 id="a"><img src="https://www.americares.org/wp-content/uploads/refresh.png" width="30px" height="30px"></h1>
	<h1 id="b"><a href="https://www.bluestacks.com/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/en/0/04/BlueStacks_Logo.png" width="240px" height="65px"></a></h1>
	<h2 id="c">Top Charts</h2><br>
	<div id = "d">Top Free Apps</div><br>""")
	applications = App.all()
	c=0
	for app in applications:
		if c==0:
			self.response.write('<p id = "app1">')
			self.response.write('<img id = "app1_img" src = "%s" width = "120px" height="120px"><br><br>' %app.app_img)
	                self.response.write('%s<br>' %app.app_name)
			self.response.write('%s<br>' %app.app_package)
			self.response.write('</p>')
		elif c==1:
			self.response.write('<p id = "app2">')
			self.response.write('<img id = "app2_img" src = "%s" width = "120px" height="120px"><br><br>' %app.app_img)
	                self.response.write('%s<br>' %app.app_name)
			self.response.write('%s<br>' %app.app_package)
			self.response.write('</p>')
		elif c==2:
			self.response.write('<p id = "app3">')
			self.response.write('<img id = "app3_img" src = "%s" width = "120px" height="120px"><br><br>' %app.app_img)
	                self.response.write('%s<br>' %app.app_name)
			self.response.write('%s<br>' %app.app_package)
			self.response.write('</p>')
		else:
			break
		c+=1
	self.response.write("""
	<br><br><br><br><br><br><br><br><br><br><br><br>
	<div id = "e">Top Reviewed</div><br><br>
	<p id = "app1">
		<img id = "app1_img" src = "" width = "120px" height="120px"><br><br>
		<br>
		
	</p>
	<p id = "app2">
		<img id = "app2_img" src = "" width = "120px" height="120px"><br><br>
		<br>
	</p>
	<p id = "app3">
		<img id = "app3_img" src = "" width = "120px" height="120px"><br><br>
		<br>
		

	</p>
	<br><br><br><br><br><br><br><br><br><br><br><br>
	<div id = "f">Top Rated</div><br><br>
	<p id = "app1">
		<img id = "app1_img" src = "" width = "90px" height="90px"><br><br>
		<br>
		
	</p>
	<p id = "app2">
		<img id = "app2_img" src = "" width = "90px" height="90px"><br><br>
		<br>
	</p>
	<p id = "app3">
		<img id = "app3_img" src = "" width = "90px" height="90px"><br><br>
		<br>
		

	</p>
</body>
</html>""")

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)


# def main():
#     from paste import httpserver
#     httpserver.serve(app, host='127.0.0.1', port='8080')


# if __name__ == '__main__':
#     main()
