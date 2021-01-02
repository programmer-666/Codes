package com.example.sqliteclassalpha;

import androidx.appcompat.app.AppCompatActivity;

import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        SQLiteDatabase sqLiteDatabase = openOrCreateDatabase("deneme.db", MODE_PRIVATE, null);
        BytecoinManagement bytecoinManagement = new BytecoinManagement(sqLiteDatabase);

        bytecoinManagement.databaseQueries.createTables();
        bytecoinManagement.userQueries.insertUser("programmer666", "qwerty");

        bytecoinManagement.closeDatabaseConnection();
    }
}