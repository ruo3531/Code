public class Stock {
    String symbol, name;
    double previousClosingPrice, currentPrice;
    public Stock(String s, String n){
        symbol = s;
        name = n;
    }
    public double getChangePercent(){
        return (currentPrice - previousClosingPrice)/previousClosingPrice*100;
    }
    public static void main(String[] args){
        Stock ANS = new Stock("ORCL", "Oracle Corporation");
        ANS.previousClosingPrice = 34.5;
        ANS.currentPrice = 34.35;
        System.out.printf("%.2f%%", ANS.getChangePercent());
    }
}
