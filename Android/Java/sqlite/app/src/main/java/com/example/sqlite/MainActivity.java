package com.example.sqlite;
import androidx.appcompat.app.AppCompatActivity;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    SQLiteDatabase conn;
    EditText username, passowrd;
    //Cursor resSet;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        username = (EditText)findViewById(R.id.editTextTextPersonName);
        passowrd = (EditText)findViewById(R.id.editTextTextPassword);
        conn = openOrCreateDatabase("database.db", MODE_PRIVATE, null);
        conn.execSQL("CREATE TABLE IF NOT EXISTS USERS(id_user INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)");
        // CURSOR
        //resSet = conn.rawQuery("SELECT * FROM USERS", null);
        // CURSOR
    }
    public void loginFunction(View view) {
        Cursor cursor = conn.rawQuery("SELECT * FROM USERS;", null);

    }
    public void registerFunction(View view){
        conn.execSQL("INSERT INTO USERS VALUES (1, '"+username.getText().toString()+"', '"+passowrd.getText().toString()+"')");
        Toast.makeText(this, "registerFunctionRunned", Toast.LENGTH_SHORT).show();
    }
}