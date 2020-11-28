package com.example.calcr;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import java.lang.Math;
import android.widget.EditText;
import android.widget.RadioGroup;
import android.widget.TextView;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {
    TextView textView;
    RadioGroup radioGroup;
    EditText e1, e2;
    int x,y;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView = (TextView)findViewById(R.id.textView);
        e1 = (EditText)findViewById(R.id.editTextNumber);
        e2 = (EditText)findViewById(R.id.editTextNumber2);
        radioGroup = (RadioGroup)findViewById(R.id.radioGroup);
        radioGroup.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                    x = Integer.parseInt(e1.getText().toString());
                    y = Integer.parseInt(e2.getText().toString());
                    if(!e1.getText().toString().isEmpty() && !e1.getText().toString().isEmpty()){
                        if(checkedId == R.id.radioButton)
                            textView.setText(String.valueOf(x+y));
                        else if(checkedId == R.id.radioButton2)
                            textView.setText(String.valueOf(x-y));
                        else if(checkedId == R.id.radioButton3)
                            textView.setText(String.valueOf(x*y));
                        else if(checkedId == R.id.radioButton4)
                            textView.setText(String.valueOf(x/y));
                        else if(checkedId == R.id.radioButton5)
                            textView.setText(String.valueOf(Math.pow(x,y)));
                        else if(checkedId == R.id.radioButton6)
                            textView.setText(String.valueOf(x%y));
                        else if(checkedId == R.id.radioButton7)
                            textView.setText(String.valueOf(Math.sqrt(x)+", "+String.valueOf(Math.sqrt(y))));
                    }
            }
        });
    }
}