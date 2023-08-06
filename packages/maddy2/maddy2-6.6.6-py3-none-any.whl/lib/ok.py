def ok():
    print("""
    
package com.example.tempcal;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
public class MainActivity extends AppCompatActivity implements View.OnClickListener {
 Button but_Add, but_Sub, but_Mul, but_Div;
 EditText txt_Num1, txt_Num2;
 TextView txt_Res;
 @Override
 protected void onCreate(Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 setContentView(R.layout.activity_main);
 but_Add = (Button) findViewById(R.id.butAdd);
 but_Sub = (Button) findViewById(R.id.butSub);
 but_Mul = (Button) findViewById(R.id.butMul);
 but_Div = (Button) findViewById(R.id.butDiv);
 txt_Num1 = (EditText) findViewById(R.id.txtNum1);
 txt_Num2 = (EditText) findViewById(R.id.txtNum2);
 txt_Res = (TextView) findViewById(R.id.txtVResult1);
 but_Add.setOnClickListener(this);
 but_Sub.setOnClickListener(this);
 but_Mul.setOnClickListener(this);
 but_Div.setOnClickListener(this);
 }
 @Override
 public void onClick(View v) {
 double Op1=Double.parseDouble(txt_Num1.getText().toString());
 double Op2=Double.parseDouble(txt_Num2.getText().toString());
 double Res;
 if (v.equals(but_Add))
 Res=Op1+Op2;
 else if(v.equals(but_Sub))
 Res=Op1-Op2;
 else if(v.equals(but_Mul))
 Res=Op1*Op2;
 else if(v.equals(but_Div))
 Res=Op1/Op2;
 else
 Res=0;
 txt_Res.setText(String.valueOf(Res));
 }
}

    """)