package com.example.bytecoindva1_0;

import androidx.appcompat.app.AppCompatActivity;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    TextView textView, byc;
    Button button, send;
    EditText u,p;
    BytecoinManagement bytecoinManagement;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        u = findViewById(R.id.editTextTextPersonName);
        p = findViewById(R.id.editTextTextPassword);

        textView = findViewById(R.id.textView);
        byc = findViewById(R.id.textViewBYCAmount);
        button = findViewById(R.id.buttonLogin);
        send = findViewById(R.id.buttonSend);

        SQLiteDatabase sqLiteDatabase = openOrCreateDatabase("bytecoin.db", MODE_PRIVATE, null);

        bytecoinManagement = new BytecoinManagement(sqLiteDatabase);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(bytecoinManagement.sessionManagement.loginControl(u.getText().toString(), p.getText().toString()) > 0){
                    byc.setText(String.valueOf(bytecoinManagement.walletQueries.getAmountByUsername(u.getText().toString())));
                }else {
                    Toast.makeText(MainActivity.this, "login failed", Toast.LENGTH_SHORT).show();
                }
            }
        });

        send.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (bytecoinManagement.walletQueries.sendBytecoin(10001, 10002, 0)){
                    Toast.makeText(MainActivity.this, "Success", Toast.LENGTH_SHORT).show();
                }else{
                    Toast.makeText(MainActivity.this, "Not Enough BYC", Toast.LENGTH_SHORT).show();
                }
            }
        });

        byc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                byc.setText(String.valueOf(bytecoinManagement.walletQueries.getAmountByUsername(u.getText().toString())));
            }
        });

        bytecoinManagement.closeDatabaseConnection();
    }
}