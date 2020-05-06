import 'package:flutter/material.dart';
import 'package:flutter_colorpicker/flutter_colorpicker.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Profile App',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool lightTheme = true;
  Color currentColor = Colors.limeAccent;

  void changeColor(Color color) => setState(() => currentColor = color);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
          body: SafeArea(
                      child: Column(
        children: <Widget>[
            Container(child: Image.asset('assets/DSC_0046.JPG')),
            Expanded(
                          child: Container(
                padding: const EdgeInsets.fromLTRB(30.0, 15.0, 30.0, 15.0),
                color: currentColor,
                child: Column(
                  children: <Widget>[
                    Text("Prakhar Bhatnagar",
                    style: TextStyle(
                      color: useWhiteForeground(currentColor) ? const Color(0xffffffff) : const Color(0xff000000),
                      fontSize: 35.0,
                      fontFamily: 'Pacifico'
                    ),
                    ),
                    Text(
                      "Flutter Developer",
                      style: TextStyle(
                        color: useWhiteForeground(currentColor) ? const Color(0xffffffff) : const Color(0xff000000),
                        fontFamily: 'Pacifico',
                        fontSize: 25.0
                      )
                    ),
                    Container(
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(25.0),
                      ),
                      padding: const EdgeInsets.symmetric(vertical: 25.0),
                      child: Column(
                        children: <Widget>[
                          TextFormField(
                            readOnly: true,
                            decoration: InputDecoration(
                              labelStyle: TextStyle(
                                fontSize: 20.0,
                                fontWeight: FontWeight.w900,
                                color: useWhiteForeground(currentColor) ? const Color(0xffffffff) : const Color(0xff000000)
                              ),
                              labelText: "Email",
                              //fillColor: Colors.white,
                              border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(25.0),
                                borderSide: BorderSide(
                                  //color: useWhiteForeground(currentColor) ? const Color(0xffffffff) : const Color(0xff000000),
                                  width: 30.0
                                )
                              ),
                            ),
                            initialValue: 'college@prakharb10.com',
                            style: TextStyle(
                              fontFamily: "Poppins",
                              color: useWhiteForeground(currentColor) ? const Color(0xffffffff) : const Color(0xff000000)
                            ),
                          ),
                        ],
                      ),
                    ),
                    TextFormField(
                      readOnly: true,
                        decoration: InputDecoration(
                          labelStyle: TextStyle(
                            fontSize: 20.0,
                            fontWeight: FontWeight.w900,
                            color: useWhiteForeground(currentColor) ? const Color(0xffffffff) : const Color(0xff000000)
                          ),
                          labelText: "Contact",
                          //fillColor: Colors.white,
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(25.0),
                            borderSide: BorderSide(
                              color: Colors.black,
                              width: 33.0
                            )
                          ),
                        ),
                        initialValue: '+91 9521416190',
                        style: TextStyle(
                          fontFamily: "Poppins",
                          color: useWhiteForeground(currentColor) ? const Color(0xffffffff) : const Color(0xff000000)
                        ),
                      ),
                    Padding(
                      padding: const EdgeInsets.only(top: 30.0),
                      child: RaisedButton(
                        elevation: 3.0,
                        onPressed: () {
                          showDialog(
                            context: context,
                            builder: (BuildContext context) {
                              return AlertDialog(
                                title: Text('Select a color'),
                                content: SingleChildScrollView(
                                  child: BlockPicker(
                                    pickerColor: currentColor,
                                    onColorChanged: changeColor,
                                  ),
                                ),
                                actions: <Widget>[
                                  FlatButton(
                                    onPressed: () {
                                      Navigator.of(context).pop();
                                    },
                                    child: const Text('Set Color')
                                  )
                                ],
                              );
                            },
                          );
                        },
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(15.0),
                          side: BorderSide(color: Colors.black)),
                        child: const Text('Change color'),
                        color: currentColor.withAlpha(100),
                        textColor: useWhiteForeground(currentColor)
                            ? const Color(0xffffffff)
                            : const Color(0xff000000),
                      ),
                    ),
                  ],
                ),
              ),
            ),
        ],
      ),
          ),
    );
  }
}
