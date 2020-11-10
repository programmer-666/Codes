package com.example.datatransfer;
//https://stackoverflow.com/questions/2091465/how-do-i-pass-data-between-activities-in-android-application
//https://stackoverflow.com/questions/11303887/how-can-i-transfer-the-data-between-two-activities-in-android
import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.material.tabs.TabLayout;

public class MainActivity extends AppCompatActivity {
    EditText usr, psw;
    Button sendButton;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        usr = (EditText)findViewById(R.id.editTextTextPersonName);
        psw = (EditText)findViewById(R.id.editTextTextPersonName2);
        sendButton = (Button)findViewById(R.id.button);
        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(usr.getText().toString().equalsIgnoreCase("programmer") && psw.getText().toString().equalsIgnoreCase("123")){
                    Intent sharpIntent = new Intent(getBaseContext(), Sharp.class);
                    sharpIntent.putExtra("username", usr.getText().toString());
                    sharpIntent.putExtra("password", psw.getText().toString());
                    startActivity(sharpIntent);
                }else{
                    Toast.makeText(MainActivity.this, "Login Failed", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}