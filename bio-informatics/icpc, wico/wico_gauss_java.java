import java.util.Random;
import java.util.Scanner;

public class Gauss{
    static private final double     z=0.0, u=1.0;
    static private final int        LCanvas=800;
    static private       double[][] f_mod, f_rec, Image;
    static private       double[]   arrExp;
    static private       int        Lx, Ly, n_max;
    static private 	 double     f_min, f_max, f_av;
    static private 	 Random     Stream;

    public static void main(String[] args){

	long seed=7777;

	double  sigma, rnl;
	int     Bx, By;
	boolean status;
	Scanner Inp;

	Inp  = new Scanner(System.in);
	System.out.print("Give Lx:");
	Lx   = Inp.nextInt();
	System.out.print("Give Ly:");
	Ly   = Inp.nextInt();
	n_max = (Lx-1)*(Lx-1) + (Ly-1)*(Ly-1);


	f_mod = new double[Lx+1][Ly+1];
	Image = new double[Lx+1][Ly+1];
	arrExp = new double[n_max+1];

	makeModel();

	checkArray(f_mod);
	Scale(f_mod, f_min, f_max);
	status = setupCanvas(1,Lx,1,Ly);
	if(status) Disp(Image);
	waitForClick(1,Lx,1,Ly);

	System.out.print("Give noise level:");
	rnl = Inp.nextDouble();
	System.out.print("Adding noise to real-space data...");
	addNoise(rnl,seed);
	System.out.println("... Done");

	checkArray(f_mod);
	Scale(f_mod, f_min, f_max);
	status = setupCanvas(1,Lx,1,Ly);
	if(status) Disp(Image);
	waitForClick(1,Lx,1,Ly);


	f_rec  = new double[Lx+1][Ly+1];

	while(true){
	System.out.print("Give sigma:");
	sigma = Inp.nextDouble();
	makeExp(sigma);
	filterGauss();

	status = setupCanvas(1,Lx,1,Ly);
	checkArray(f_rec);
	Scale(f_rec, f_min, f_max);
	Disp(Image);
	}

    } // End method main


    public static void makeModel(){
	int i, j, Mx, My, Rx, Ry;

	Mx = (Lx-1)/2; Rx = Mx/2;
	My = (Ly-1)/2; Ry = My/2;

	for(i=1; i<=Lx; i++){
	for(j=1; j<=Ly; j++){
	    if      (i-1  <= 3) f_mod[i][j] = 0;
	    else if (Lx-i <= 3) f_mod[i][j] = 0;
	    else if (j-1  <= 3) f_mod[i][j] = 0;
	    else if (Ly-j <= 3) f_mod[i][j] = 0;
	    else if (Math.abs(i-Mx) <= Rx   && 
                     Math.abs(j-My) <= Ry   && 
                     Math.abs(i-Mx) >= Rx/2 && 
                     Math.abs(j-My) >= Ry/2 ) 
		f_mod[i][j] = 1;
	    else 
		f_mod[i][j] = 0.5*i/Lx;
}}

    } // end method makeModel


    public static void filterGauss(){
	int i, j, k, l, n;


	for(i=1; i<=Lx; i++){
	for(j=1; j<=Ly; j++){
	    f_rec[i][j]=0.0;
	for(k=1; k<=Lx; k++){
	for(l=1; l<=Ly; l++){
	    n = (i-k)*(i-k)+(j-l)*(j-l);

	    f_rec[i][j] = f_rec[i][j] + arrExp[n] * f_mod[k][l];

		}}}}

    } // end method filterGauss

    public static void makeExp(double sigma){
	int n;
	double sigma_2;

	sigma_2 = sigma*sigma;

	for(n=0; n<=n_max; n++){
	    arrExp[n] = Math.exp(-n/sigma_2);
	}

    } // end method filterGauss

    public static void checkArray(double[][] f){
	int    i, j;
	double fij;

	f_min=f[1][1]; f_max=f[1][1]; f_av=z; 
	for(i=1; i<=Lx; i++){
	for(j=1; j<=Ly; j++){
	    fij = f[i][j];
	    f_av = f_av + Math.abs(fij);
	    if(f[i][j]<f_min) f_min=f[i][j];
	    if(f[i][j]>f_max) f_max=f[i][j];
	}}
	f_av  = f_av/(Lx*Ly);

    } // End method checkArray


    public static void addNoise(double rnl, long seed){
	int i,j;

	Stream = new Random(seed);

	checkArray(f_mod);
	
	for(i=1; i<=Lx; i++){
	for(j=1; j<=Ly; j++){
	    f_mod[i][j] = f_mod[i][j] + rnl*f_av*(Stream.nextDouble()-0.5);
	}}

    }




    public static void Scale(double[][] f, double f1, double f2){
	int i, j;
	double fij, range, val;
	range = f2-f1;

	for(i=1; i<=Lx; i++){
	for(j=1; j<=Ly; j++){
	    fij =  f[i][j];
	    val = (fij - f1) / range;
	    if(val < z) val=z;
	    if(val > u) val=u;
	    Image[i][j] = val;
	}}

    } // End method Scale


    public static boolean setupCanvas(int I1, int I2, int J1, int J2){
	int LLx, LLy, dLLx, dLLy;
	double ar;
	
	if(I1<1) {
	    System.out.println("setupCanvas error I1<1");
	    return false;}
	
	if(I1>=I2) {
	    System.out.println("setupCanvas error I1>=I2");
	    return false;}

	if(J1<1) {
	    System.out.println("setupCanvas error J1<1");
	    return false;}
	
	if(J1>=J2) {
	    System.out.println("setupCanvas error J1>=J2");
	    return false;}

	LLx = I2-I1+1;
	LLy = J2-J1+1;
	dLLx = Math.max(1, LLx/50);
	dLLy = Math.max(1, LLy/50);

	ar = (double)LLy / (double)LLx;
	if     (ar< u){LLx=LCanvas; LLy=(int)((double)LCanvas/ar);}
	else if(ar==u){LLx=LCanvas; LLy=LCanvas;}
	else if(ar> u){LLy=LCanvas; LLx=(int)((double)LCanvas/ar);}

	StdDraw.enableDoubleBuffering();
	StdDraw.setCanvasSize(LLx,LLy);
	StdDraw.setXscale(I1-dLLx, I2+dLLx);
        StdDraw.setYscale(J1-dLLy, J2+dLLy);
	return true;
	
    } // End method setupCanvas	
	

    public static void Disp(double[][] f){
	int i, j, alpha;

        StdDraw.clear(StdDraw.GREEN);
	for(i=1; i<=Lx; i++){
	for(j=1; j<=Ly; j++){
	    alpha = (int) (255.0*f[i][j]);
	    StdDraw.setPenColor(alpha, alpha, alpha);
	    StdDraw.filledSquare(i,j,1);
	}}

	StdDraw.show();

    } // End method Disp
    

    public static void waitForClick(int I1, int I2, int J1, int J2){
	boolean flag=true;
	int i,j;
	
	while(flag){
	if(StdDraw.isMousePressed()){
	i = (int)(StdDraw.mouseX()+0.5);
	j = (int)(StdDraw.mouseY()+0.5);
	flag = !(i>=I1 && i<=I2 && j>=J1 && j<=J2);}}
	
    } // End method waitForClick

    
} // End class FT
