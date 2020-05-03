import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  

  
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      

  
  List<Color> _colorsb = [ //Get list of colors
    Colors.deepPurple,
    Colors.indigo,
    Colors.blue,
    Colors.green,
    Colors.yellow,
    Colors.orange,
    Colors.red
    
  ];

  int _currentIndex = 0;
  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      //appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        //title: Text(widget.title),
        //backgroundColor: _colorsb[_currentIndex],
      //),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Invoke "debug painting" (press "p" in the console, choose the
          // "Toggle Debug Paint" action from the Flutter Inspector in Android
          // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
          // to see the wireframe for each widget.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          mainAxisAlignment: MainAxisAlignment.center,
          
          children: <Widget>[
            
          new Container(
          width: 180.0,
          height: 180.0,
          decoration: new BoxDecoration(
          shape: BoxShape.circle,
          image: new DecorationImage(
          fit: BoxFit.fill,
          image: new AssetImage(
                 "images/profile1.jpg")
                 )
          )),
           /*Image.asset('images/profile.jpg',
           width: 200,
           height: 200,
           
           ),*/
            
            Text(
              'Vedant Rishi Das',
              style: TextStyle(
               fontSize: 50,
              color: Colors.white,
              fontStyle: FontStyle.italic,
              fontWeight: FontWeight.bold,
            ),
            ),
            Padding(padding: EdgeInsets.only(
                        top: 7.0, bottom: 7.0, right: 40.0, left: 7.0),),
            Text(
              'Flutter Developer',
              style: TextStyle(fontSize: 30,color: Colors.white,fontStyle: FontStyle.italic,fontWeight: FontWeight.bold,)
            ),
            Padding(padding: EdgeInsets.only(
                        top: 7.0, bottom: 7.0, right: 40.0, left: 7.0),),
            
           /* new RaisedButton(
            elevation : 0.0,
           shape: new RoundedRectangleBorder(
                        borderRadius: new BorderRadius.circular(30.0)),
                    padding: EdgeInsets.only(
                        top: 7.0, bottom: 7.0, right: 30.0, left: 7.0),
            onPressed: null,
            color: Colors.white,
           child: new Row(children: <Widget>[
             new Image.asset('images/phone2.png',height:40, width:40,),
             Padding(
                            padding: EdgeInsets.only(left: 10.0),
                            child: new Text(
                              "+919556503585",
                              style: TextStyle(
                                  fontSize: 20.0, color: Colors.white ),
                            ))
           ],), 
           ),*/

           Padding(padding: EdgeInsets.only(
                        top: 7.0, bottom: 7.0, right: 40.0, left: 7.0),),
          /* new RaisedButton(elevation : 0.0,
           shape: new RoundedRectangleBorder(
                        borderRadius: new BorderRadius.circular(30.0)),
                    padding: EdgeInsets.only(
                        top: 7.0, bottom: 7.0, right: 30.0, left: 7.0),
            onPressed: null,
           child: new Row(children: <Widget>[
             new Image.asset('images/email.png',height:40, width:40,),
             Padding(
                            padding: EdgeInsets.only(left: 10.0),
                            child: new Text(
                              "vedant.das1@learner.manipal.edu",
                              style: TextStyle(
                                  fontSize: 20.0,color: Colors.white ),
                            ))
           ],), 
           color: Colors.white,
           
           ),*/

          Padding(
              padding: const EdgeInsets.fromLTRB(30.0, 20.0, 30.0, 10.0),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(5.0),
                child: Container(
                  color: Colors.white,
                  child: ListTile(
                    leading: Icon(
                      Icons.phone_android,
                      color: _colorsb[_currentIndex],
                    ),
                    title: Text(
                      "YOUR PHONE NUMBER",
                      style: TextStyle(color: _colorsb[_currentIndex]),
                    ),
                  ),
                ),
              ),
),
            Padding(
              padding: const EdgeInsets.fromLTRB(30.0, 20.0, 30.0, 10.0),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(5.0),
                child: Container(
                  color: Colors.white,
                  child: ListTile(
                    leading: Icon(
                      Icons.email,
                      color: _colorsb[_currentIndex],
                    ),
                    title: Text(
                      "YOUR EMAIL",
                      style: TextStyle(color: _colorsb[_currentIndex]),
                    ),
                  ),
                ),
              ),
),
            new ButtonTheme.bar(
              child: new ButtonBar(
              alignment: MainAxisAlignment.center,
              children: <Widget>[
                
                Container(
              width: 30,
              child: new RaisedButton(onPressed: (){setState(() {
                _currentIndex=0;
                
              });},
              
              color: _colorsb[0],),
            ),
            Container(
              width: 30,
              child: new RaisedButton(onPressed: (){setState(() {
                _currentIndex=1;
              });},
              color: _colorsb[1],),
            ),
            Container(
              width: 30,
              child: new RaisedButton(onPressed: (){setState(() {
                _currentIndex=2;
              });},
              color: _colorsb[2],),
            ),
            Container(
              width: 30,
              child: new RaisedButton(onPressed: (){setState(() {
                _currentIndex=3;
              });},
              color: _colorsb[3],),
            ),
            Container(
              width: 30,
              child: new RaisedButton(onPressed: (){setState(() {
                _currentIndex=4;
              });},
              color: _colorsb[4],),
            ),
            Container(
              width: 30,
              child: new RaisedButton(onPressed: (){setState(() {
                _currentIndex=5;
              });},
              color: _colorsb[5],),
            ),
            Container(
              width: 30,
              child: new RaisedButton(onPressed: (){setState(() {
                _currentIndex=6;
              });},
              color: _colorsb[6],),
            ),
                  ],
        ),
        )
          ],
        ),
      ),
      backgroundColor: _colorsb[_currentIndex],
      //floatingActionButton: FloatingActionButton(
        //onPressed: _incrementCounter,
        //tooltip: 'Increment',
        //child: Icon(Icons.add),
      //), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
