package com.example.databasetest;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.bytecoinmanagement.BytecoinManagement;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MainActivity extends AppCompatActivity {
    EditText username, password;
    Button loginButton;
    String token;
    boolean loginFlag = false;
    BytecoinManagement bytecoinManagement;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        username = (EditText)findViewById(R.id.usernameEditText);
        password = (EditText)findViewById(R.id.passwordEditText);
        loginButton = (Button)findViewById(R.id.loginButton);
        loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                loginControl(username, password);
            }
        });
    }
    // DATABASE PROCS
    SQLiteDatabase connection;
    String dbname = "bytecoin_demo.db";
    public void databaseConnection(){
        this.connection = openOrCreateDatabase(dbname,MODE_PRIVATE,null);
    }
    public void databaseDisconnect(){
        this.connection.close();
    }
    public void createTables(){
        this.connection.execSQL("CREATE TABLE IF NOT EXISTS USERS (id_user INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)");
        this.connection.execSQL("CREATE TABLE IF NOT EXISTS WALLETS (id_wallet INTEGER PRIMARY KEY, id_user INTEGER NOT NULL REFERENCES USERS(id_user), bytecoin REAL NOT NULL)");
    }
    public void insertUser(String username, String password){
        this.connection.execSQL("INSERT INTO USERS (username, password) VALUES ('"+username+"', '"+getMD5(password)+"')");
    }
    public String getMD5(String input) {
        try{
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(input.getBytes());
            BigInteger number = new BigInteger(1, messageDigest);
            String hashtext = number.toString(16);
            while (hashtext.length() < 32){hashtext = "0" + hashtext;}
            return hashtext;}
        catch (NoSuchAlgorithmException e){throw new RuntimeException(e);}
    }
    public int getTableLen(String table_name){
        Cursor cursor = connection.rawQuery("SELECT COUNT(*) FROM "+table_name+"",null);
        cursor.moveToFirst();
        return Integer.parseInt(cursor.getString(0).toString());
    }
    // DATABASE PROCS
    // LOGIN CONTROL
    public void loginControl(EditText _username, EditText _password){
        databaseConnection();
        Cursor cur = connection.rawQuery("SELECT * FROM USERS", null);
        for(int i = 0;i<getTableLen("USERS");i++){
            cur.moveToPosition(i);
            if(cur.getString(1).toString().equalsIgnoreCase(_username.getText().toString()) && cur.getString(2).toString().equalsIgnoreCase(getMD5(password.getText().toString()))){
                loginFlag = true;
                break;
            }else{
                loginFlag = false;
            }
        }
        if(loginFlag){
            // yonlendir
            //Toast.makeText(this, "Login Success", Toast.LENGTH_SHORT).show();
            Intent sharpIntent = new Intent(getBaseContext(), statusActivity.class);
            startActivity(sharpIntent);
        }else{
            Toast.makeText(this, "Login Failed", Toast.LENGTH_SHORT).show();
        }
        databaseDisconnect();
    }
    // LOGIN CONTROL
}
