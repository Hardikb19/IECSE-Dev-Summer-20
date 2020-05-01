import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  var col = Colors.blue;
  var colarr = [Colors.blue, Colors.yellow, Colors.amber, Colors.red, Colors.purple, Colors.orange, Colors.teal];
  var counter = 1;
  final ImageProvider img = AssetImage('assets/pic.jpeg');
  Widget photoGraph(){
    Size size = MediaQuery.of(context).size;
    return Container(
      alignment: Alignment.center,
      height: size.height*0.225,
      width: size.height*0.225,
      margin: EdgeInsets.all(15.0),
      padding: EdgeInsets.zero,
      decoration: BoxDecoration(
        color: Colors.white,
        shape: BoxShape.rectangle,
        borderRadius: BorderRadius.all(Radius.circular(100)),
        border: Border.all(width: 3,color: Colors.white,style: BorderStyle.solid),
        image: DecorationImage(image: img),
        ),
      );
  }

  Widget details(String det, var ic){
    Size size = MediaQuery.of(context).size;
    return Container(
      margin: EdgeInsets.all(10.0),
      height: size.height*0.08,
      width: size.width*0.8,
      alignment: Alignment.center,
      padding: EdgeInsets.all(8.0),
      decoration: BoxDecoration(
        color: Colors.white,
        shape: BoxShape.rectangle,
        borderRadius: BorderRadius.all(Radius.circular(10)),
        border: Border.all(width: 3,color: col,style: BorderStyle.solid),
      ),
      child: Row(
        children: [
          Icon(
            ic,
            color: col,
            size: 20.0,
          ),
          Text(
            '   $det',
            textAlign: TextAlign.center,
            style: TextStyle(
              fontSize: 17.0,
              color: col,
            ),
          )
        ],
      ),
    );
  }

  Widget changeColor(var colorIndex){
    Size size = MediaQuery.of(context).size;
    return GestureDetector(
      child: Container(
        margin: EdgeInsets.all(8.0),
        height: size.height*0.04,
        width: size.width*0.1,
        alignment: Alignment.center,
        padding: EdgeInsets.all(8.0),
        decoration: BoxDecoration(
          color: colarr[colorIndex],
          shape: BoxShape.rectangle,
          borderRadius: BorderRadius.all(Radius.circular(10)),
          border: Border.all(width: 3,color: Colors.white,style: BorderStyle.solid),
        ),
      ),
      onTap: (){
        setState(() {
          col = colarr[colorIndex];
        });
      },
    );
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: col,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[            
            photoGraph(),
            Text(
              'Abhinav Agrawal',
              textAlign: TextAlign.center,
              style: TextStyle(
                color: Colors.white,
                fontSize: 40.0,
                fontFamily: 'DancingScript'
              ),
            ),
            Text(
              'Flutter Developer',
              textAlign: TextAlign.center,
              style: TextStyle(
                color: Colors.white,
                fontSize: 30.0,
                fontFamily: 'DancingScript'
              ),
            ),
            details('+918169809401', Icons.phone_android),
            details('abhinav.hfs@gmail.com', Icons.email),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                changeColor(0),
                changeColor(1),
                changeColor(2),
                changeColor(3),
                changeColor(4),
                changeColor(5),
                changeColor(6),
              ],
            )
          ],
        ),
      ),
    );
  }
}

