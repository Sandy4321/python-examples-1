Reverse Encryption
------------------

This level is about reversing an encryption algorithm. 

The original text is a bunch of fake serial numbers. Click here to see some examples of what they look like. The PHP-code which is used for the encryption is given below:




    <?php

      //-----------------------------------------
      function evalCrossTotal($strMD5)
      {
          $intTotal = 0;
          $arrMD5Chars = str_split($strMD5, 1);
          foreach ($arrMD5Chars as $value)
          {
              $intTotal += '0x0'.$value;
          }
          return $intTotal;
      }//-----------------------------------------


      //-------------------------------------------
      function encryptString($strString, $strPassword)
      {
          // $strString is the content of the entire file with serials
          $strPasswordMD5 = md5($strPassword);
          $intMD5Total = evalCrossTotal($strPasswordMD5);
          $arrEncryptedValues = array();
          $intStrlen = strlen($strString);
          for ($i=0; $i<$intStrlen; $i++)
          {
              $arrEncryptedValues[] =  ord(substr($strString, $i, 1))
                                       +  ('0x0' . substr($strPasswordMD5, $i%32, 1))
                                       -  $intMD5Total;
              $intMD5Total = evalCrossTotal(substr(md5(substr($strString,0,$i+1)), 0, 16)
                                       .  substr(md5($intMD5Total), 0, 16));
          }
          return implode(' ' , $arrEncryptedValues);
      }//--------------------------------------------

    ?> 


This is the encrypted text:

-175 -150 -180 -212 -97 -197 -144 -185 -129 -156 -143 -232 -176 -143 -155 -192 -201 -164 -204 -209 -163 -144 -203 -186 -127 -164 -135 -181 -109 -156 -178 -159 -177 -183 -205 -181 -114 -168 -181 -214 -164 -166 -168 -208 -139 -140 -103 -187 -185 -145 -197 -167 -199 -143 -186 -179 -182 -215 -144 -228 -143 -117 -143 -178 -122 -170 -88 -140 -132 -162 -148 -186 -131 -160 -128 -150 -216 -165 -137 -241 -120 -181 -144 -224 -133 -148 -183 -165 -116 -208 -145 -110 -202 -165 -186 -181 -171 -148 -177 -229


Send the last one of the serial numbers you decrypted as answer.

You have 120 seconds time to send the solution.
