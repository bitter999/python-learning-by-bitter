/*安全加密程序v1.0
*作者:bitter
*联系方式:
*/
//引入头文件用的。标准的输入输出
#include <stdio.h> 
// 字符串 提供了一些字符串要用到的函数
#include <string.h> 
//系统函数
#include <stdlib.h>
#include <ctype.h>

/*声明一些变量*/
char ch = '0';
char filename[256]="";//保存输入的数据 文件的路径
FILE *fp =NULL;
FILE *fptemp =NULL;
char password[12] = "123456";
const char tempfile[256] = "temp123456789.temp";
int pwdlen =0;
int i = 0;

/*函数声明*/
void menu();
void inputpass(char *pass);


/*函数实现*/
void inputpass(char *pass)
{
    scanf("%s",pass);
}

void menu()
{
    printf("****************************************\n");
    printf("****************安全课程小程序*****************\n");
    printf("****************************************\n");
    printf("**请输入要加密或者解密的文件的路径**\n");
    printf("**例如:/user/bitter/av.txt**\n"); //注意这里是linux下的路径，win系统需要反斜杠路径
    /*步骤一:要打开一个文件或目录*/
    /*通过字符终端读取一个字符串*/
    gets(filename);
    if( NULL == (fp = fopen(filename,"rb")))
    {
        /*如果不为空 表示文件存在，空的 表示文件不存在*/
        printf("你好你输入的文件不存在\n");
        //退出
        exit(1);

    }
    /*如果密码存在*/
    printf("文件存在。你好请你输入密码，如:123456\n");
    inputpass(password);
    pwdlen = (int)strlen(password);
    if( 0 == pwdlen )
    {
         printf("对不起！密码长度不能为0.\n");
        //退出
        exit(2);
    }
    /*步骤二:读出文件中的内容进行加密*/
    fptemp = fopen(tempfile,"wb");

    /*步骤三:把加密的信息写入到文件中覆盖原来的*/
    while(1)
    {
        ch = getc(fp);
        if(feof(fp))
        {
            /*判断文件读完没有*/
            break;
        }
        /*每取出一个字符串就加密*/
        ch^=password[i++];
        //ch就是加密之后的数据了
        fputc(ch,fptemp);
        //判断
        if(i == pwdlen)
        {
            i = 0;
        }
    }
    //循环结束之后，清理
    fclose(fp);
    fclose(fptemp);
    remove(filename);
    rename(tempfile,filename);
    printf("恭喜你加密或解密成功\n");
}



//主函数 是c语言程序的入口地址
int main(int argc,char const *argv[])
{
  // 函数调用
    menu();
    return 0;
}