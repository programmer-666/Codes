package com.example.bytecoinmanagementtest;

import androidx.appcompat.app.AppCompatActivity;

import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;

import com.example.bytecoinmanagement.BytecoinManagement;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        SQLiteDatabase sqLiteDatabase = openOrCreateDatabase("denemetest.db", MODE_PRIVATE, null);
        BytecoinManagement bytecoinManagement = new BytecoinManagement(sqLiteDatabase);
        bytecoinManagement.databaseQueries.createTables();
    }
}