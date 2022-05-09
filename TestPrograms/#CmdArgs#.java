public class CmdArgs {
   public static void main(String[] args) {

   }
}

https://accsindia-my.sharepoint.com/:x:/g/personal/rprustagi_accsindia_org/ETSB-IOn2qFHsLFX8rDUBd4BwsYLzDq36jPg9_jt5k6NLA?e=VKcBwW

https://meetingsapac3.webex.com/meetingsapac3/j.php?MTID=m132dc53628ba261e0103ecdfdd06541f

https://meetingsapac3.webex.com/meetingsapac3/j.php?MTID=m71e54fbe04cacd6afb65b75098f41507


indraramyadav770@gmail.com
ramyayadav770@gmail.com

kumarpavan1309@gmail.com



xval=[i for i in range(cnt)]
yval=[m*i + c for i in range(cnt)]
plt.plot(xval, yval,label="y=mx+c")
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Graph for y=" + str(m) + "x+" + str(c))
plt.legend()
plt.show()


cnt=200
xmax = 4*math.pi
x=[xmax*i/cnt for i in range(cnt)]
y0=[0 for i in range(cnt)]
y1=[math.sin(xmax*i/cnt) for i in range(cnt)]
y2=[math.cos(xmax*i/cnt) for i in range(cnt)]

plt.plot(x,y0,'k--', label="baseline")
plt.plot(x,y1,'b.', label="Sin" +r'$\theta$')
plt.plot(x,y2,'g.', label="Cos" +r'$\theta$')
plt.xlabel(r"$\theta$ values")
plt.ylabel("Sin and cos curves")
plt.xticks([i*math.pi for i in range(5)],
    [r'$0$', r'$\pi$', r'$2\pi$',r'$3\pi$',r'$4\pi$'])
plt.legend()
plt.show()

