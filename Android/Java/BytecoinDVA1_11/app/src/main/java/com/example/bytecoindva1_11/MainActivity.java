package com.example.bytecoindva1_11;

import androidx.appcompat.app.AppCompatActivity;

import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    TextView textView;
    BytecoinManagement bytecoinManagement;
    Button buttonCC;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        buttonCC = findViewById(R.id.buttonCloseConn);
        textView = findViewById(R.id.textView);
        SQLiteDatabase sqLiteDatabase = openOrCreateDatabase("test.db", MODE_PRIVATE, null);
        bytecoinManagement = new BytecoinManagement(sqLiteDatabase);
        //bytecoinManagement.databaseQueries.createTables();
        //bytecoinManagement.userQueries.insertUser("programmer666", "qwerty");

        textView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (bytecoinManagement.walletQueries.sendBytecoin(1001, 1002, 10)){
                    Toast.makeText(MainActivity.this, "sended", Toast.LENGTH_SHORT).show();
                }else{
                    Toast.makeText(MainActivity.this, "not sended", Toast.LENGTH_SHORT).show();
                }
            }
        });

        buttonCC.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                bytecoinManagement.closeDatabaseConnection();
            }
        });

    }
}