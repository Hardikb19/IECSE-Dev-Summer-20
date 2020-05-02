import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'IECSE Profile Page',
      home: ProfilePage(),
    );
  }
}

class ProfilePage extends StatefulWidget {
  @override
  _ProfilePageState createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  Color _appColor = Colors.purpleAccent;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: _appColor,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Container(
              width: 100.0,
              height: 100.0,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                image: DecorationImage(
                  image: AssetImage('assets/profile-pic.jpg'),
                ),
                border: Border.all(color: Colors.white),
              ),
            ),
            SizedBox(height: 20.0),
            Text(
              'Adit Luhadia',
              style: TextStyle(
                color: Colors.white,
                fontWeight: FontWeight.bold,
                fontSize: 30.0,
              ),
            ),
            SizedBox(height: 20.0),
            Text(
              'FLUTTER DEVELOPER',
              style: TextStyle(
                color: Colors.white,
                fontSize: 20.0,
              ),
            ),
            SizedBox(height: 20.0),
            infoTile(icon: Icons.phone_android, title: '+91 9351496916'),
            infoTile(icon: Icons.mail, title: 'aditluhadia@allmityapp.tk'),
            SizedBox(height: 20.0),
            Row(
              mainAxisSize: MainAxisSize.min,
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                colorButton(Colors.purpleAccent),
                colorButton(Colors.indigo),
                colorButton(Colors.blue),
                colorButton(Colors.green),
                colorButton(Colors.yellow),
                colorButton(Colors.orange),
                colorButton(Colors.red),
              ],
            ),
          ],
        ),
      ),
    );
  }

  /// Creates an info tile.
  ///
  /// The `icon` and `title` arguments must not be `null`.
  ///
  /// Example:
  ///
  /// ```dart
  ///   infoTile(icon: Icons.mail, title: 'aditluhadia@allmityapp.tk')
  /// ```
  Widget infoTile({@required IconData icon, @required String title}) {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: 20.0),
      child: Card(
        child: ListTile(
          leading: Icon(
            icon,
            color: _appColor,
          ),
          title: Text(
            title,
            style: TextStyle(color: _appColor),
          ),
        ),
      ),
    );
  }

  /// Returns a color button.
  ///
  /// The `color` argument takes a `Color`.
  ///
  /// Example:
  ///
  /// ```dart
  ///   colorButton(Colors.purpleAccent)
  /// ```
  Widget colorButton(Color color) {
    return Container(
      height: 18.0,
      width: 18.0,
      decoration: BoxDecoration(
        border: Border.all(
          color: Colors.white,
        ),
      ),
      child: FlatButton(
        color: color,
        onPressed: () => _changeColor(color),
        child: null,
      ),
    );
  }

  /// Returns `null`.
  ///
  /// Changes the primary color of the application.
  ///
  /// Example:
  ///
  /// ```dart
  ///   _changeColor(Colors.red);
  /// ```
  void _changeColor(Color color) {
    setState(() {
      _appColor = color;
    });
  }
}
