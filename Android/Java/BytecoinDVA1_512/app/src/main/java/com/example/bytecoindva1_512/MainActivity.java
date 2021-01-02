package com.example.bytecoindva1_512;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    BytecoinManagement bytecoinManagement;
    SQLiteDatabase sqLiteDatabase;

    EditText username, password;
    Button buttonLogin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        username = findViewById(R.id.username);
        password = findViewById(R.id.password);
        buttonLogin = findViewById(R.id.buttonLogin);


        buttonLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sqLiteDatabase = openOrCreateDatabase("bytecoin_dva1_512.db", MODE_PRIVATE, null);
                bytecoinManagement = new BytecoinManagement(sqLiteDatabase);

                if (bytecoinManagement.sessionManagement.loginControl(username.getText().toString(), password.getText().toString())){
                    Intent bycmain = new Intent(getBaseContext(), bycmain.class);
                    bycmain.putExtra("username", username.getText().toString());
                    bycmain.putExtra("password", password.getText().toString());
                    startActivity(bycmain);
                }else{
                    Toast.makeText(MainActivity.this, "Login Failed", Toast.LENGTH_SHORT).show();
                }

                bytecoinManagement.closeDatabaseConnection();
            }
        });

    }
}