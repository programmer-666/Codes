package com.example.bytecoin;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    EditText usernameEditText, passwordEditText;
    Button loginButton;

    SQLiteDatabase sqLiteDatabase;
    BytecoinManagement bytecoinManagement;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // CREATING DATABASE
        /*
        sqLiteDatabase = openOrCreateDatabase("bytecoin.db", MODE_PRIVATE, null);
        bytecoinManagement = new BytecoinManagement(sqLiteDatabase);
        bytecoinManagement.databaseQueries.createTables();
        bytecoinManagement.userQueries.insertUser("_Technician", "q123");
        bytecoinManagement.userQueries.insertUser("JamesBond", "y123");
        bytecoinManagement.closeDatabaseConnection();
        */
        // CREATING DATABASE

        usernameEditText = findViewById(R.id.usernameEditText);
        passwordEditText = findViewById(R.id.passwordEditText);

        loginButton = findViewById(R.id.loginButton);

        loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sqLiteDatabase = openOrCreateDatabase("bytecoin.db", MODE_PRIVATE, null);
                bytecoinManagement = new BytecoinManagement(sqLiteDatabase);

                if (bytecoinManagement.sessionManagement.loginControl(usernameEditText.getText().toString(), passwordEditText.getText().toString())){

                    Intent bytecoinMain = new Intent(getBaseContext(), bytecoinMain.class);
                    bytecoinMain.putExtra("username", usernameEditText.getText().toString());
                    bytecoinMain.putExtra("password", passwordEditText.getText().toString());
                    startActivity(bytecoinMain);

                }else{
                    Toast.makeText(MainActivity.this, "Login Failed", Toast.LENGTH_SHORT).show();
                }

                bytecoinManagement.closeDatabaseConnection();
            }
        });

    }
}