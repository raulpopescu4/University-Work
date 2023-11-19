import 'package:sqflite/sqflite.dart' as sql;
import 'package:intl/intl.dart';

class SQLHelper{
  static Future<void> createTables(sql.Database database) async{
    await database.execute("""CREATE TABLE calories(
      date DATE PRIMARY KEY NOT NULL,
      amount INTEGER,
      carbohydrates INTEGER,
      fats INTEGER,
      protein INTEGER
    )""");
  }

  static Future<sql.Database> db() async{
    return sql.openDatabase(
      "calories_db.db",
      version: 1,
      onCreate: (sql.Database database, int version) async{
        await createTables(database);
      }
    );

  }

  static Future<String> createTable(var date, String amount, String carbohydrates, String fats, String protein) async{
    final db =  await SQLHelper.db();

    final DateTime parsedDate = DateTime.parse(date);

    final calories = {
      'date': DateFormat('yyyy-MM-dd').format(parsedDate),
      'amount': amount,
      'carbohydrates': carbohydrates,
      'fats': fats,
      'protein': protein
    };
    final returnDate = await db.insert('calories', calories, conflictAlgorithm: sql.ConflictAlgorithm.replace);

    return returnDate.toString();
  }

  static Future<List<Map<String, dynamic>>> getAllTables() async{
    final db = await SQLHelper.db();
    return db.query('calories', orderBy: 'date');
  }

  static Future<List<Map<String, dynamic>>> getSingleTable(var date) async{
    final db = await SQLHelper.db();
    return db.query('calories', where: "date = ?", whereArgs: [DateFormat('yyyy-MM-dd').format(date)], limit: 1);
  }

  static Future<int> updateTable(var date, String amount, String carbohydrates, String fats, String protein) async{
    final db = await SQLHelper.db();

    final DateTime parsedDate = DateTime.parse(date);

    final calories = {
      'date': DateFormat('yyyy-MM-dd').format(parsedDate),
      'amount': amount,
      'carbohydrates': carbohydrates,
      'fats': fats,
      'protein': protein
    };
    final result = await db.update('calories', calories, where: "date = ?", whereArgs: [DateFormat('yyyy-MM-dd').format(parsedDate)]);
    return result;
  }

  static Future<void> deleteTable(var date) async{
    final db = await SQLHelper.db();

    final DateTime parsedDate = DateTime.parse(date);

    try{
      await db.delete('calories', where: "date = ?", whereArgs: [DateFormat('yyyy-MM-dd').format(parsedDate)]);
    } catch (e){}
  }

}