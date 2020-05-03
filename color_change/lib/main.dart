import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
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
 int _r = 0;
 int _g = 0;
 int _b = 0;

  
  void _changered() {
    setState(() {
      _r =222;
      _g = 41;
      _b = 59;
    });
  }

 void _changegreen() {
    setState(() {
      _r = 153;
      _g = 255;
      _b = 51;
    });
  }

  void _changeblue() {
    setState(() {
      _r = 55;
      _g = 224;
      _b = 243;
    });
  }

  void _changepurple() {
    setState(() {
      _r = 187;
      _g = 55;
      _b = 243;
    });
  }

  void _changeorange() {
    setState(() {
      _r = 255;
      _g = 128;
      _b = 0;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color.fromRGBO(_r, _g, _b,5.0),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Container(
              child: ClipOval(
                child: Image.asset(
                  'images/ik.jpg',
                  width: 130.0,
                  height: 130.0,
                  fit: BoxFit.cover,
                ),
              ),
              decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  border: Border.all(color: Colors.white, width: 3.0)),
            ),
            SizedBox(height: 25.0),
            Text(
              'Ishan K.',
              style: TextStyle(
                color: Colors.white,
                fontSize: 50.0,
                fontFamily: 'Pacifico',
              ),
            ),
            SizedBox(height: 25.0),
            Text(
              'FLUTTER DEVELOPER ',
              style: TextStyle(
                fontFamily: 'Electrolize',
                color: Colors.white,
                fontSize: 25.0,
              ),
            ),
            SizedBox(height: 25.0),
            Container(
              width: 300.0,
              child: Card(
                child: ListTile(
                  leading: Icon(Icons.phone_android,
                  color: Color.fromRGBO(_r, _g, _b,5.0),
                  ),
                  title: Text('9430470186',
                  style: TextStyle(
                    color: Color.fromRGBO(_r, _g, _b,5.0),
                  ),
                  
                  ),
                ),
              ),
            ),
            SizedBox(height: 15.0),
            Container(
              width: 300.0,
              child: Card(
                child: ListTile(
                  leading: Icon(Icons.mail,
                  color: Color.fromRGBO(_r, _g, _b,5.0),
                  ),
                  title: Text('itsik159@gmail.com',
                  style: TextStyle(
              color: Color.fromRGBO(_r, _g, _b,5.0),

                  ),
                  ),
                ),
              ),
            ),
            SizedBox(height: 25.0),
            Container(
              width: 200.0,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: <Widget>[
                  SizedBox(
                    width: 25.0,
                    child: FloatingActionButton(
                      backgroundColor: Color.fromRGBO(222, 41, 59, 5.0),
                      onPressed: () {
                        _changered();
                      },
                    ),
                  ),
                  SizedBox(
                    width: 25.0,
                    child: FloatingActionButton(
                      backgroundColor: Color.fromRGBO(153, 255, 51, 5.0),
                      onPressed: () {
                        _changegreen();
                      },
                    ),
                  ),
                  SizedBox(
                    width: 25.0,
                    child: FloatingActionButton(
                      backgroundColor: Color.fromRGBO(55, 224, 243, 5.0),
                      onPressed: () {
                        _changeblue();
                      },
                    ),
                  ),
                  SizedBox(
                    width: 25.0,
                    child: FloatingActionButton(
                      backgroundColor: Color.fromRGBO(187, 55, 243, 5.0),
                      onPressed: () {
                        _changepurple();
                      },
                    ),
                  ),
                  SizedBox(
                    width: 25.0,
                    child: FloatingActionButton(
                      backgroundColor: Color.fromRGBO(255, 128, 0, 5.0),
                      onPressed: () {
                        _changeorange();
                      },
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      // floatingActionButton: FloatingActionButton(
      //   onPressed: _incrementCounter,
      //   tooltip: 'Increment',
      //   child: Icon(Icons.add),
      // ),
    );
  }
}
