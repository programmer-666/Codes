package com.example.sqlitedatabaseclasstest;

import androidx.appcompat.app.AppCompatActivity;

import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    Button button, closeb;
    TextView textView;
    SQLiteDatabase con;
    BytecoinMain bytecoinMain;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button = findViewById(R.id.button);
        closeb = findViewById(R.id.buttonClose);
        textView = findViewById(R.id.textView);

        con = openOrCreateDatabase("deneme.db", MODE_PRIVATE,  null);
        bytecoinMain = new BytecoinMain(con, textView);
        bytecoinMain.databaseQueries.createTables();

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                bytecoinMain.databaseQueries.userQueries.insertUser("programmer666", "qwerty");
            }
        });

        textView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textView.setText(""+bytecoinMain.databaseQueries.getTableLen("USERS")+" - "+bytecoinMain.databaseQueries.getTableLen("WALLETS"));
            }
        });

        closeb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                bytecoinMain.closeConnection();
            }
        });
    }
}