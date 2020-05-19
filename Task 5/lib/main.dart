import 'package:flutter/material.dart';
import 'dart:async';

import 'package:dio/dio.dart';
void main() => runApp(MyApp());
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Search App',
      home: MyCustomForm(),
      debugShowCheckedModeBanner: false,
    );
  }
}

// Define a custom Form widget.
class MyCustomForm extends StatefulWidget {
  @override
  _MyCustomFormState createState() => _MyCustomFormState();
}

// Define a corresponding State class.
// This class holds the data related to the Form.
class _MyCustomFormState extends State<MyCustomForm> {
  // Create a text controller and use it to retrieve the current value
  // of the TextField.
  final myController = TextEditingController();

  var searchText;
  Dio dio = new Dio();
  Response response;
  var url = "http://skullycoder1709.pythonanywhere.com/wiki/getInfo";
  List<String> rec = [];

  Future<String> _sendInfo(text) async{
    response = await dio.post(url, data: {"name" : text});
    return response.data["info"].toString();
  }

  Widget getListView(){
    var listView = ListView.builder(
      itemBuilder: (context, index){
        return ListTile(
          leading: Icon(Icons.search),
          title: Text(rec[index]),
          onTap: (){
            Navigator.push(context, MaterialPageRoute(builder: (context) => InfoPage(rec[index], showInfo(rec[index]))));
          },
        );
      },
      itemCount: rec.length,

    );
    return listView;
  }
  Widget showInfo(text){
    return FutureBuilder(
      future: _sendInfo(text),
      builder: (BuildContext context, AsyncSnapshot snapshot){
        if(snapshot.data != null){
          return Container(
            padding: EdgeInsets.all(12.0),
            child: Text(
              snapshot.data,
              style: TextStyle(
                 fontSize: 20.0,
              ),
            ),
          );
        }
        else{
          return Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              CircularProgressIndicator()
            ],
          );
        }
      },
    );
  }
  @override
  void dispose() {
    myController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Wikipedia', style: TextStyle(
          color: Colors.black
        ),),
        backgroundColor: Colors.white70,
        centerTitle: true,
      ),
      body: SingleChildScrollView( 
        scrollDirection: Axis.vertical,        
        child: Column(
        children: [
          Container(
            padding: EdgeInsets.all(24.0),
            child: Image(
              image: AssetImage('assets/wiki.jfif')
              ),
          ),
          Container(
            padding: EdgeInsets.all(12.0),
            child: TextField(
              decoration: InputDecoration(
                hintText: "Enter Search Keyword",

                suffixIcon:  GestureDetector(
                  child: Container(
                    height: 5.0,
                    width: 5.0,
                    child: Icon(Icons.search),
                      decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(50.0),
                    ),
                  ),
                  onTap: (){
                    searchText = myController.text;
                    if(searchText!=""){
                      rec.add(searchText);
                      print(rec);
                      Navigator.push(context, MaterialPageRoute(builder: (context) => InfoPage(searchText, showInfo(searchText))));
                    }
                  },
                ),
              ),
              controller: myController,
            ),
          ),
          GestureDetector(
            child: Container(
              child: Text(
                "See Recent Searches",
                style: TextStyle(
                  fontWeight: FontWeight.bold
                ), 
              ),
              height: 40.0,
              padding: EdgeInsets.all(12.0),
              decoration: BoxDecoration(
                border: Border.all(color: Colors.black),
                borderRadius: BorderRadius.circular(10.0),
              ),
            ),
            onTap: (){
              Navigator.push(context, MaterialPageRoute(builder: (context) => RecentSearches(getListView())));
            },
          )
        ],
      ),
      )
      );
  }
}

class InfoPage extends StatelessWidget{
  final String name;
  final Widget info;
  InfoPage(this.name, this.info);
  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        title: Text(name),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                padding: EdgeInsets.all(12.0),
                child: Text(
                  '$name: ',
                  textAlign: TextAlign.left,
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 45.0
                  ),
                ),
              ),
              info
            ],
          ),
      ),
    );
  }
}

class RecentSearches extends StatelessWidget{
  final Widget content;
  RecentSearches(this.content);

  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(title: Text("Recent Searches"),),
      body: content,
    );
  }
}