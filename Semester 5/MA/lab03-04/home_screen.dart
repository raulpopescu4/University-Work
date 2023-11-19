import 'package:calorie_tracker_app/db_helper.dart';
import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget{
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {

  List<Map<String, dynamic>> _allData = [];

  bool _isLoading = true;

  void _refreshData() async{
    final data = await SQLHelper.getAllTables();
    setState(() {
      _allData = data;
      _isLoading = false;
    });
  }

  @override
  void initState(){
    super.initState();
    _refreshData();
  }

  Future<void> _addCalories() async{
    await SQLHelper.createTable(_dateController.text, _amountController.text, _carbohydratesController.text, _fatsController.text, _proteinController.text);
    _refreshData();
  }

  Future<void> _updateCalories(var date) async{
    await SQLHelper.updateTable(date, _amountController.text, _carbohydratesController.text, _fatsController.text, _proteinController.text);
    _refreshData();
  }

  void _deleteData(var date) async{
    await SQLHelper.deleteTable(date);
    ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
      backgroundColor: Colors.redAccent,
      content: Text("Entry deleted"),
    ));
    _refreshData();
  }

  final TextEditingController _dateController = TextEditingController();
  final TextEditingController _amountController = TextEditingController();
  final TextEditingController _carbohydratesController = TextEditingController();
  final TextEditingController _fatsController = TextEditingController();
  final TextEditingController _proteinController = TextEditingController();

  void showBottomSheet(var date) async{
    if(date != null){
      final existingData = _allData.firstWhere((element) => element['date'] == date);
      _dateController.text = existingData['date'];
      _amountController.text = existingData['amount'].toString();
      _carbohydratesController.text = existingData['carbohydrates'].toString();
      _fatsController.text = existingData['fats'].toString();
      _proteinController.text = existingData['protein'].toString();
    }

    showModalBottomSheet(
      elevation: 5,
      isScrollControlled: true,
      context: context,
      builder: (_) => Container(
        padding: EdgeInsets.only(
          top: 30,
          left: 15,
          right: 15,
          bottom: MediaQuery.of(context).viewInsets.bottom + 50,

        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.end,
          children: [
            TextField(
              controller: _dateController,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                hintText: "Date",
              ),
            ),
            SizedBox(height: 10),
            TextField(
              controller: _amountController,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                hintText: "Amount",
              ),
            ),
            SizedBox(height: 10),
            TextField(
              controller: _carbohydratesController,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                hintText: "Carbohydrates",
              ),
            ),
            SizedBox(height: 10),
            TextField(
              controller: _fatsController,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                hintText: "Fats",
              ),
            ),
            SizedBox(height: 10),
            TextField(
              controller: _proteinController,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                hintText: "Protein",
              ),
            ),
            SizedBox(height: 10),

            Center(
              child: ElevatedButton(
                onPressed: () async{
                  if (date == null){
                    await _addCalories();
                  }
                  else{
                    await _updateCalories(date);
                  }

                  _dateController.text = "";
                  _amountController.text = "";
                  _carbohydratesController.text = "";
                  _fatsController.text = "";
                  _proteinController.text = "";

                  Navigator.of(context).pop();
                  print("Calories Added");
                },
                child: Padding(
                  padding: EdgeInsets.all(18),
                  child: Text(date == null ? "Add Calories" : "Update",
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.w500,
                  ),),
                ),
              ),
            )
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context){
    return Scaffold(
      backgroundColor: Colors.white54,
      appBar: AppBar(
        title: Text("Calories Tracker"),
      ),
      body: _isLoading ? Center(child: CircularProgressIndicator(),): ListView.builder(
        itemCount: _allData.length,
          itemBuilder: (context, index) => Card(
            margin: EdgeInsets.all(15),
            child: ListTile(
              title: Padding(
                padding: EdgeInsets.symmetric(vertical: 5),
                child: Text(_allData[index]['date'],
                style: TextStyle(
                  fontSize: 20,
                  ),
                ),
              ),
              subtitle: Text(_allData[index]['amount'].toString()),
              trailing: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  IconButton(
                    onPressed: (){
                      showBottomSheet(_allData[index]['date']);
                    },
                    icon: Icon(
                    Icons.edit,
                    color: Colors.amber,
                  ),
               ),
                  IconButton(
                    onPressed: (){
                      _deleteData(_allData[index]['date']);
                    },
                    icon: Icon(
                      Icons.delete,
                      color: Colors.redAccent,
                    ),
                  ),
                ],
              ),
            ),
          ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => showBottomSheet(null),
        child: Icon(Icons.add),
      ),
    );
  }
}