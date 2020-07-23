import webapp2
import sys
sys.path.insert(0, 'libs')
from bs4 import BeautifulSoup
import urllib2
from google.appengine.ext import db


class TopFree(db.Model):
    app_img = db.StringProperty(required=True)
    app_name = db.StringProperty(required=True)
    app_pub = db.StringProperty(required=True)
    app_package = db.StringProperty(required=True)


# url = "https://play.google.com/store/apps/top?hl=en_IN"
# html_content = requests.get(url).text


# def App_key(app_package=None):
#   return db.Key.from_path('App', app_package)

response = urllib2.urlopen('https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU&hl=en_IN')
#response = urllib2.urlopen('https://play.google.com/store/apps/top?hl=en_IN')
html_content = response.read()
soup = BeautifulSoup(html_content, "lxml")
top_free_apps = soup.find_all(attrs={"class": "ImZGtf mpg5gc"})
for i in top_free_apps:
    img = i.find_all("img")
    name = i.find_all(attrs={"class": "WsMG1c"})
    pub = i.find_all(attrs={"class": "KoLSrc"})
    package = i.find_all(attrs={"class": "poRVub"})
    obj = TopFree(app_img=img[0]["data-src"], app_name=name[0].text, app_pub=pub[0].text[:20],
              app_package=package[0]["href"][23:])
    obj.put()
    # print(app_img[0]["data-src"])
    # print(app_name[0].text)


class TopGross(db.Model):
    app_img = db.StringProperty(required=True)
    app_name = db.StringProperty(required=True)
    app_pub = db.StringProperty(required=True)
    app_package = db.StringProperty(required=True)


response2 = urllib2.urlopen('https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF3RvcGdyb3NzaW5nX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljLe6QA&gsr=CiLSDh8KHQoXdG9wZ3Jvc3NpbmdfQVBQTElDQVRJT04QBxgD:S:ANO1ljKx5Ik&hl=en_IN')
#response2 = urllib2.urlopen('https://play.google.com/store/apps/top?hl=en_IN')
html_content2 = response2.read()
soup2 = BeautifulSoup(html_content2, "lxml")
top_grossing_apps = soup2.find_all(attrs={"class": "ImZGtf mpg5gc"})
for i in top_grossing_apps:
    img = i.find_all("img")
    name = i.find_all(attrs={"class": "WsMG1c"})
    pub = i.find_all(attrs={"class": "KoLSrc"})
    package = i.find_all(attrs={"class": "poRVub"})
    obj2 = TopGross(app_img=img[0]["data-src"], app_name=name[0].text, app_pub=pub[0].text[:20],
              app_package=package[0]["href"][23:])
    obj2.put()


class TopGames(db.Model):
    app_img = db.StringProperty(required=True)
    app_name = db.StringProperty(required=True)
    app_pub = db.StringProperty(required=True)
    app_package = db.StringProperty(required=True)


response3 = urllib2.urlopen('https://play.google.com/store/apps/collection/cluster?clp=0g4YChYKEHRvcGdyb3NzaW5nX0dBTUUQBxgD:S:ANO1ljLhYwQ&gsr=ChvSDhgKFgoQdG9wZ3Jvc3NpbmdfR0FNRRAHGAM%3D:S:ANO1ljIKta8&hl=en_IN')
#response3 = urllib2.urlopen('https://play.google.com/store/apps/top?hl=en_IN')
html_content3 = response3.read()
soup3 = BeautifulSoup(html_content3, "lxml")
top_games = soup3.find_all(attrs={"class": "ImZGtf mpg5gc"})
for i in top_games:
    img = i.find_all("img")
    name = i.find_all(attrs={"class": "WsMG1c"})
    pub = i.find_all(attrs={"class": "KoLSrc"})
    package = i.find_all(attrs={"class": "poRVub"})
    obj3 = TopGames(app_img=img[0]["data-src"], app_name=name[0].text, app_pub=pub[0].text[:20],
              app_package=package[0]["href"][23:])
    obj3.put()


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
        font-family: Georgia, serif;
        color:#b1cdcd;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-top: 10px;
        padding-top: 0px;
        text-shadow: 2px 2px 4px #000000;
        }
        #d{
        font-family: "Trebuchet MS", Helvetica, sans-serif;
        margin-left: 20px;
        color: white;
        font-size: 30px;
        padding-left: 50px;
        }
        #e{
        font-family: "Trebuchet MS", Helvetica, sans-serif;
        margin-left: 20px;
        color:white;
        font-size: 30px;
        padding-left: 50px;
        }
        #f{
        font-family: "Trebuchet MS", Helvetica, sans-serif;
        margin-left: 20px;
        color:white;
        font-size: 30px;
        padding-left: 50px;
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
        #app4_img{
        border-radius: 20%;
        }
        #app5_img{
        border-radius: 20%;
        }
        #app6_img{
        border-radius: 20%;
        }
        #app1{
	margin-left: 30px;
	margin-right: 150px;
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
	margin-left: 30px;
	float:right;
	text-align:top;
	border-width:2px;
	border-color:red;
	height:150px;
	width : 150px;
	color : white;
	text-align: center;
	border-radius: 25px;
        }
        #app3{
	margin-left: 30px;
	float:right;
	text-align:top;
	border-width:2px;
	border-color:red;
	height:150px;
	width : 150px;
	color : white;
	text-align: center;
	border-radius: 20px;
        }
        #app4{
	margin-left: 30px;
	float:right;
	text-align:top;
	border-width:2px;
	border-color:red;
	height:150px;
	width : 150px;
	color : white;
	text-align: center;
	border-radius: 20px;
        }
        #app5{
	margin-left: 30px;
	float:right;
	text-align:top;
	border-width:2px;
	border-color:red;
	height:150px;
	width : 150px;
	color : white;
	text-align: center;
	border-radius: 20px;
        }
        #app6{
	float:right;
	text-align:top;
	border-width:2px;
	border-color:red;
	height:150px;
	width : 150px;
	color : white;
	text-align: center;
	border-radius: 20px;
        }
        </style>
        <title>WebApp</title>
</head>
<body>
<h1 id="a"><img src="https://www.americares.org/wp-content/uploads/refresh.png" width="30px" height="30px"></h1>
<h1 id="b"><a href="https://www.bluestacks.com/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/en/0/04/BlueStacks_Logo.png" width="240px" height="65px"></a></h1>
<h2 id="c">Top Charts</h2><br>
<div id = "d">Top Free Apps</div><br>""")
        applications = TopFree.all()
        c = 0
        for app in applications:
            if c == 0:
                self.response.write('<p id = "app1">')
                self.response.write(
                    '<img id = "app1_img" src = "%s" width = "120px" height="120px"><br><br>' % app.app_img)
                self.response.write('%s<br>' % app.app_name)
                self.response.write('%s<br>' %app.app_pub)
                self.response.write('</p>')
            elif c == 1:
                self.response.write('<p id = "app2">')
                self.response.write(
                    '<img id = "app2_img" src = "%s" width = "120px" height="120px"><br><br>' % app.app_img)
                self.response.write('%s<br>' % app.app_name)
                self.response.write('%s<br>' %app.app_pub)
                self.response.write('</p>')
            elif c == 2:
                self.response.write('<p id = "app3">')
                self.response.write(
                    '<img id = "app3_img" src = "%s" width = "120px" height="120px"><br><br>' % app.app_img)
                self.response.write('%s<br>' % app.app_name)
                self.response.write('%s<br>' %app.app_pub)
                self.response.write('</p>')
            elif c == 3:
                self.response.write('<p id = "app4">')
                self.response.write(
                    '<img id = "app4_img" src = "%s" width = "120px" height="120px"><br><br>' % app.app_img)
                self.response.write('%s<br>' % app.app_name)
                self.response.write('%s<br>' %app.app_pub)
                self.response.write('</p>')
            elif c == 4:
                self.response.write('<p id = "app5">')
                self.response.write(
                    '<img id = "app5_img" src = "%s" width = "120px" height="120px"><br><br>' % app.app_img)
                self.response.write('%s<br>' % app.app_name)
                self.response.write('%s<br>' %app.app_pub)
                self.response.write('</p>')
            elif c == 5:
                self.response.write('<p id = "app6">')
                self.response.write(
                    '<img id = "app6_img" src = "%s" width = "120px" height="120px"><br><br>' % app.app_img)
                self.response.write('%s<br>' % app.app_name)
                self.response.write('%s<br>' %app.app_pub)
                self.response.write('</p>')
            else:
                break
            c += 1
        self.response.write("""
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        <div id = "e">Top Grossing</div><br><br>""")
        top_gross = TopGross.all()
        c = 0
        for gross in top_gross:
            if c==0:
                self.response.write('<p id = "app1">')
                self.response.write(
                    '<img id = "app1_img" src = "%s" width = "120px" height="120px"><br><br>' % gross.app_img)
                self.response.write('%s<br>' % gross.app_name)
                self.response.write('%s<br>' %gross.app_pub)
                self.response.write('</p>')
            elif c == 1:
                self.response.write('<p id = "app2">')
                self.response.write(
                    '<img id = "app2_img" src = "%s" width = "120px" height="120px"><br><br>' % gross.app_img)
                self.response.write('%s<br>' % gross.app_name)
                self.response.write('%s<br>' %gross.app_pub)
                self.response.write('</p>')
            elif c == 2:
                self.response.write('<p id = "app3">')
                self.response.write(
                    '<img id = "app3_img" src = "%s" width = "120px" height="120px"><br><br>' % gross.app_img)
                self.response.write('%s<br>' % gross.app_name)
                self.response.write('%s<br>' %gross.app_pub)
                self.response.write('</p>')
            elif c == 3:
                self.response.write('<p id = "app4">')
                self.response.write(
                    '<img id = "app4_img" src = "%s" width = "120px" height="120px"><br><br>' % gross.app_img)
                self.response.write('%s<br>' % gross.app_name)
                self.response.write('%s<br>' %gross.app_pub)
                self.response.write('</p>')
            elif c == 4:
                self.response.write('<p id = "app5">')
                self.response.write(
                    '<img id = "app5_img" src = "%s" width = "120px" height="120px"><br><br>' %gross.app_img)
                self.response.write('%s<br>' % gross.app_name)
                self.response.write('%s<br>' %gross.app_pub)
                self.response.write('</p>')
            elif c == 5:
                self.response.write('<p id = "app6">')
                self.response.write(
                    '<img id = "app6_img" src = "%s" width = "120px" height="120px"><br><br>' % gross.app_img)
                self.response.write('%s<br>' % gross.app_name)
                self.response.write('%s<br>' %gross.app_pub)
                self.response.write('</p>')
            else:
                break
            c += 1
        self.response.write("""
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        <div id = "f">Top Games</div><br><br>""")
        games = TopGames.all()
        c = 0
        for game in games:
            if c==0:
                self.response.write('<p id = "app1">')
                self.response.write(
                    '<img id = "app1_img" src = "%s" width = "120px" height="120px"><br><br>' % game.app_img)
                self.response.write('%s<br>' % game.app_name)
                self.response.write('%s<br>' %game.app_pub)
                self.response.write('</p>')
            elif c == 1:
                self.response.write('<p id = "app2">')
                self.response.write(
                    '<img id = "app2_img" src = "%s" width = "120px" height="120px"><br><br>' % game.app_img)
                self.response.write('%s<br>' % game.app_name)
                self.response.write('%s<br>' %game.app_pub)
                self.response.write('</p>')
            elif c == 2:
                self.response.write('<p id = "app3">')
                self.response.write(
                    '<img id = "app3_img" src = "%s" width = "120px" height="120px"><br><br>' % game.app_img)
                self.response.write('%s<br>' % game.app_name)
                self.response.write('%s<br>' %game.app_pub)
                self.response.write('</p>')
            elif c == 3:
                self.response.write('<p id = "app4">')
                self.response.write(
                    '<img id = "app4_img" src = "%s" width = "120px" height="120px"><br><br>' % game.app_img)
                self.response.write('%s<br>' % game.app_name)
                self.response.write('%s<br>' %game.app_pub)
                self.response.write('</p>')
            elif c == 4:
                self.response.write('<p id = "app5">')
                self.response.write(
                    '<img id = "app5_img" src = "%s" width = "120px" height="120px"><br><br>' % game.app_img)
                self.response.write('%s<br>' % game.app_name)
                self.response.write('%s<br>' %game.app_pub)
                self.response.write('</p>')
            elif c == 5:
                self.response.write('<p id = "app6">')
                self.response.write(
                    '<img id = "app6_img" src = "%s" width = "120px" height="120px"><br><br>' % game.app_img)
                self.response.write('%s<br>' % game.app_name)
                self.response.write('%s<br>' %game.app_pub)
                self.response.write('</p>')
            else:
                break
            c += 1
        self.response.write("""
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

