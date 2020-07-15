import webapp2
#from bs4 import BeautifulSoup
#import requests
from google.appengine.ext import db

# class app(db.model):
#     app_img = db.StringProperty(required=True)
#     app_name = db.StringProperty(required=True)

# url = "https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU&hl=en_IN"
# html_content = requests.get(url).text

# soup = BeautifulSoup(html_content, "lxml")
# top_free_apps = soup.find_all(attrs = { "class" : "ImZGtf mpg5gc"})
# for i in top_free_apps:
#     img = i.find_all("img")
#     name = i.find_all(attrs={"class": "KoLSrc"})
#     obj = app(app_img = img, app_name = name)
#     obj.put()
#     # print(app_img[0]["data-src"])
#     # print(app_name[0].text)
class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
<html>
<head>
        <link type="text/css" rel="stylesheets" href="/stylesheets/style.css" />
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
	box-shadow: 10px 10px black;
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
	color:#507c7c;
	font-size: 30px;
	padding-left: 50px;
}
#e{
	color:#507c7c;
	font-size: 30px;
	padding-left: 50px;
}
#f{
	color:#507c7c;
	font-size: 30px;
	padding-left: 50px;
}
</style>
	<meta charset="utf-8">
	<title>WebApp</title>

</head>
<body>
	<h1 id="a"><img src="https://www.americares.org/wp-content/uploads/refresh.png" width="30px" height="30px"></h1>
	<h1 id="b"><a href="https://www.bluestacks.com/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/en/0/04/BlueStacks_Logo.png" width="240px" height="65px"></a></h1>
	<h2 id="c">Top Charts</h2>
	<div id = "d">Top Paid</div><br><br>
	<div id = "e">Top Downloaded</div><br><br>
	<div id = "f">Top Rated</div><br><br>
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
