public class HelloWorld{

    public static void main(String []args){
       
       int arr[];  
       arr = new int[101];
       
       for(int i = 1;i<101;i++)
       {
           arr[i] = 3;//2 means closed;3 means opened;
       }
       
      //Out(arr,100);
      
      int n = 2;
      int nn = 0;
      
      for(int i = 0;i<99;i++)
      {
          nn = n;
          if(n!=100)
          {
              Change(arr,101,n,nn);
          }
          else
          {
               Result(arr,101);
               System.exit(0);
          }
          n = n+1;
          
      }

       
    }
    
    public static void Change(int arr[],int len,int n,int nn)
    {
        nn = n;
        for(int i=0;i<(len/nn);i++)
        {
            for(int j = 0;j<(len/nn);j++)
            {
                
               if(arr[n] == 2)
                {
                    arr[n] = 3;
                }
                else   if (arr[n] == 3)
                      {
                       arr[n] = 2;
                       continue;
                      } 
                      n += n ;
            }
            nn += nn;
            n = nn;
        }
    }
    
    
    public static void Result(int arr[], int len)
    {
        for (int i = 1;i<len;i++)
        {
            if(arr[i] == 3)
            {
               System.out.println(i);
            }
           
        }
    }
    
    
}