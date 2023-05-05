#python Final Proj
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import time

img_contact_form = Image.open("images/pc.jpg")
ryzen5600x = Image.open("images/ryzen5600x.webp")
ryzen55600g = Image.open('images/Ryzen55600g.png')
i913900k = Image.open("images/i913900k.png")
ryzen77600x = Image.open("images/ryzen77600x.png")
i71300k = Image.open("images/i71300k.png")
B550m = Image.open("images/B550M.png")
B650m = Image.open("images/B650M.png")
Z690 = Image.open("images/Z690.png")
H510M = Image.open("images/H510M.png")
B660M = Image.open("images/B660M.png")
TeamG = Image.open("images/TeamG.png")
Cor = Image.open("images/Corsair.webp")
Z5 = Image.open("images/Z5.webp")
Gskill = Image.open("images/Gskill.png")
DDR5 = Image.open("images/DDR5.webp")
r6600xt = Image.open("images/6600xt.png")
G1660S = Image.open("images/1660S.png")
R4070 = Image.open("images/4070.png")
R7900 = Image.open("images/7900.png")
R3060 = Image.open("images/3060ti.png")
st.set_page_config(page_title="Group 6", page_icon=":desktop_computer:", layout='wide')





add_selectbox = st.sidebar.selectbox(
    "Choose a Computer Parts",
    ("Home", "CPU", "Motherboard", "RAM", "Graphics Card")
)



if "Home" in add_selectbox:
    with st.container():
        st.subheader(f"WELCOMEE:wave:")
        st.title("YOUR BEST GUIDING SITE FOR BUILDING COMPUTERS")

    with st.container():
        st.write("---" )
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("WHAT'S IN OUR SITE")
            st.write("##")
            st.write(
                """
                We will guide you on building your first system unit
                - Computer parts specification for better gaming/work experience
                - Pros and Cons of every computer parts
                """
            )

        with right_column:
            st.image(img_contact_form)




if "CPU" in add_selectbox:
    with st.container():
        st.title(":black[_CPU SELECTION_]")
        st.write(
            """ BEST CPU RECOMMENDATION
            """
        ),

        st.write("[RYZEN 5 5600g](https://bluearm.ph/products/amd-ryzen-5-5600g-3-9ghz-6core-12thd-16mb-am4-tray-type-with-hsf?variant=42927781675167&currency=PHP&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organichttps://bluearm.ph/products/amd-ryzen-5-5600g-3-9ghz-6core-12thd-16mb-am4-tray-type-with-hsf?variant=42927781675167&currency=PHP&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic)")
        st.image(ryzen55600g, width=250)
        st.write(
            """
            The AMD Ryzen 5 5600G is a Zen 3-based, desktop-grade APU featuring the Radeon Vega 7 graphics adapter. 
            This Ryzen 5 was unveiled in H1 2021. It features six SMT-enabled CPU cores for 12 threads in total, running at 3.9 GHz to 4.4 GHz. The CPU ships with AMD's Wraith Stealth cooler as long as it's not an OEM
            """),
        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Strong gaming performance on integrated graphics
                - Priced aggressively in AMD's own CPU stack
                - Regularly beats out competition from Intel
                - Wraith Stealth cooler included in the box
                - Compatible with Radeon Software suite
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Slightly slower integrated-graphics gaming performance than Ryzen 7 5700G
                - Limited motherboard compatibility at launch
                """
             )
               
        


       
        st.write("[Intel Core i9-13900k](https://ecommerce.datablitz.com.ph/products/intel-core-i9-13900k-13th-gen-3-0ghz-24-core-lga-1700-processor-bx8071513900k)"),
        st. image(i913900k, width= 300)
        st.write(
            """
            The Intel Core i9-13900K is a fast high-end desktop processor of the Raptor Lake series. 
            It includes a hybrid architecture for the CPU cores with combined 24 cores and 32 threads.
            """
        ),

        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Great raw performance; overclockable
                - Impressive gaming performance
                - More affordable than the AMD flagship
                - Support for Z690 motherboards
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Runs rather hot; requires top-notch cooling solution
                - Power consumption can exceed 250W limit
                """
             )

       

       
        st.write(
            """
        [Ryzen5 5600x](https://easypc.com.ph/products/amd-ryzen-5-5600x-socket-am4-3-7ghz-processor?variant=42048021823659&currency=PHP&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic)
        """
        ),
        st.image(ryzen5600x, width=500)
        st.write(
            """The AMD Ryzen 5 7600X is a fast mid-range desktop processor of the Raphael series. It offers 6 cores based on the Zen 4 architecture that supports hyperthreading (12 threads).
            The cores clock from 4.7 (base) up to 5.7 GHz (single core boost). When all 6 cores are fully loaded, 5.3 GHz is the max.

            """
        ),
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Huge IPC gains
                - Gaming performance improved by over 15%
                - Very power efficient
                - Bundled cooler
                - Beats 8-core 3800XT in both compute and gaming
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Price increase over previous generation
                """
             )

       
        st.write("[RYZEN 5 7600x](https://www.newegg.com/global/ph-en/amd-ryzen-5-7600x-ryzen-5-7000-series/p/N82E16819113770?item=N82E16819113770&nm_mc=knc-googlephadwords-global&cm_mmc=knc-googlephadwords-global-_-processors%20-%20desktops-_-amd-_-19113770&source=region&srsltid=Ad5pg_GKVhMzEHk8Mtt6cv1acaGoZSBOiVOt6uE3LYOgEemh1_ivcioUmLQ)"),
        st.image(ryzen77600x, width= 240)
        st.write("""The AMD Ryzen 5 7600X is a fast mid-range desktop processor of the Raphael series. It offers 6 cores based on the Zen 4 architecture that supports hyperthreading (12 threads).The cores clock from 4.7 (base) up to 5.7 GHz (single core boost). When all 6 cores are fully loaded, 5.3 GHz is the max.

            """
        ),
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Most affordable Zen 4 processor
                - Impressive performance improvements in all areas
                - New AM5 socket has lots of life ahead of it
                - Support for DDR5 and PCIE 5.0
                - Good gaming performance
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - High platform cost
                - Demanding cooling requirements / high temperatures
                - Requires a new motherboard and new RAM
                - Default 105 W TDP uses more power and generates more heat with little-to-no real performance benefit
                - Subpar multi-core performance
                """
             )

        st.write("[ Intel Core i7-13700K](https://www.newegg.com/global/ph-en/intel-core-i7-13700k-core-i7-13th-gen/p/N82E16819118414?item=N82E16819118414&nm_mc=knc-googlephadwords-global&cm_mmc=knc-googlephadwords-global-_-processors%20-%20desktops-_-intel-_-19118414&source=region&srsltid=Ad5pg_Ev_CloOboKt_velz7MV0Kbou-qJ2QXHsqyfeIP-UtvRcENlFCOfHM)"),
        st.image(i71300k, width=500)
        st.write(
            """
            The Intel Core i7-13700K is a desktop processor with 16 cores, launched in September 2022. It is part of the Core i7 lineup, using the Raptor Lake architecture with Socket 1700. 
            Thanks to Intel Hyper-Threading the core-count is effectively doubled, to 24 threads. Core i7-13700K has 30MB of L3 cache and operates at 3.4 GHz by default, but can boost up to 5.4 GHz, depending on the workload. 
            Intel is making the Core i7-13700K on a 10 nm production node, the transistor count is unknown. You may freely adjust the unlocked multiplier on Core i7-13700K, which simplifies overclocking greatly, as you can easily dial in any overclocking frequency.
             """
        ),
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - DDR4 and DDR5 support
                - Impressive performance
                - Supported on previous gen motherboards
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - AMD is faster in some cases
                - Offers similar performance to the 7900X at 4K
                - Draws a lot of power
                """
             )


if "Motherboard" in add_selectbox:
     with st.container():
        st.title(":black[_MOTHERBOARD SELECTION_]")
        st.write(
            """ BEST MOTHERBOARD RECOMMENDATION
            """
        )
        st.write('[ASUS TUF Gaming B550M - Plus](https://www.lazada.com.ph/products/easypc-asus-tuf-gaming-b550m-plus-wifi-ii-am4-ddr4-motherboard-i3669180898-s19223178862.html?spm=a2o4l.tm80167379.7779702790.1.4a4aRDdORDdOfy.4a4aRDdORDdOfy&priceCompare=skuId%3A19223178862%3Bsource%3Alazada-om%3Bsn%3A1288342f-df3b-4c9b-8354-8fa341c2e2a7%3BoriginPrice%3A1047500%3BvoucherPrice%3A1037500%3Btimestamp%3A1683213319314%3BsearchDisctDet%3A%5B%7B%22discountValue%22%3A10000%2C%22toolCode%22%3A%22shopCoupon%22%2C%22voucherChannelId%22%3A1%2C%22voucherId%22%3A900000013820042%7D%5D)')
        st.image(B550m, width=250)
        st.write(
            """
            The ASUS TUF Gaming B550M-Plus is a brilliant mid-tier motherboard with extended functionality. ou get 2.5Gb LAN, Wi-Fi 6, PCIe 4.0, and the ability to overclock even a Ryzen 9 3900X processor.
             All this on a compact MicroATX form factor.
            """
        )

        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Stable board with top-notch Wi-Fi and 2.5Gbit LAN
                - Overall well-built and well-priced from retailers
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Not the most affordable MicroATX B550 motherboard
                - Some gratuitous software utilities
                """
             )
        
        st.write('[ASUS TUF Gaming B650M-PLUS](https://www.lazada.com.ph/products/tuf-gaming-b650m-plus-b550m-plus-wifi-ii-amd-socket-am5-motherboard-for-asus-i2093285065-s18643734013.html?spm=a2o4l.tm80167379.7779702790.1.3e7aAySFAySFnl.3e7aAySFAySFnl&priceCompare=skuId%3A18643734013%3Bsource%3Alazada-om%3Bsn%3A3d46eaad-fa03-4635-a259-73f978e32678%3BoriginPrice%3A979900%3BvoucherPrice%3A979900%3Btimestamp%3A1683214268823)')
        st.image(B650m, width=250)
        st.write(
            """
            The ASUS TUF Gaming B650M-PLUS is a great choice for those looking for a Micro-ATX gaming motherboard on a budget.The ASUS TUF Gaming B650M-PLUS supports the latest DDR5 RAM, with a total 128GB capacity. It also supports the latest Ryzen 7000 series processors from AMD too. In addition, it features Wi-Fi 6 and Bluetooth 5.2, offering impressive connectivity. 
            """
        )

        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - DDR5 support
                - Perfect for smaller builds
                - Screwless M.2 sockets
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Fairly expensive for a budget motherboard
                """
             )
        
        st.write('[GIGABYTE Z690 AORUS Elite](https://www.lazada.com.ph/products/tuf-gaming-b650m-plus-b550m-plus-wifi-ii-amd-socket-am5-motherboard-for-asus-i2093285065-s18643734013.html?spm=a2o4l.tm80167379.7779702790.1.3e7aAySFAySFnl.3e7aAySFAySFnl&priceCompare=skuId%3A18643734013%3Bsource%3Alazada-om%3Bsn%3A3d46eaad-fa03-4635-a259-73f978e32678%3BoriginPrice%3A979900%3BvoucherPrice%3A979900%3Btimestamp%3A1683214268823)')
        st.image(Z690, width=250)
        st.write(
            """
            The GIGABYTE Z690 AORUS Elite comes at an extremely reasonable price, while still offering tons of great features.
            With quad NVMe M.2 slots, the GIGABYTE Z690 AORUS Elite is perfect not only for housing multiple SSDs, but also running the latest next-gen games at lightning speeds, with little loading time. That's not the only thing that will be fast, with Wi-Fi 6 and Bluetooth 5.0 enabled, you can connect multiple devices and run online games at super speed.
            """
        )
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Stunning design
                - Incredible value for money
                - Four M.2 slots
                - Wi-Fi 6 and Bluetooth built-in
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - No DDR5 support
                """
             )
        
        st.write('[ASUS Prime H510M-E](https://shopee.ph/product/30058821/11417251111)')
        st.image(H510M, width=250)
        st.write(
            """
            The ASUS Prime H510M-E might not be the flashiest gaming motherboard on the market. Similarly, it doesn't have the latest and greatest features, but it is perfect for those looking for a low to mid-range gaming motherboard on a tight budget. With a built-in M.2 slot, you can still leverage faster storage, but you'll need to pay out more on a single M.2 NVMe drive with plenty of capacity rather than smaller storage options.
            This budget motherboard is great if you need something that isn't going to break the bank but does offer DDR4 compatibility            """
        )
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Very affordable price
                - Perfect for smaller cases
                - Includes one M.2 slot
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Supports older 10th/11th gen CPUs
                - Not enough USB ports
                """
             )
        
        st.write('[Gigabyte B660M DS3H](https://www.lazada.com.ph/products/gigabyte-b660m-ds3h-ax-ddr4-lga1700-motherboard-i3000266793-s14724547963.html?spm=a2o4l.tm80167379.7779702790.1.7812J2ouJ2ouQB.7812J2ouJ2ouQB&priceCompare=skuId%3A14724547963%3Bsource%3Alazada-om%3Bsn%3Acbbe7941-1bb3-4d1b-a4d7-2cce2f49a921%3BoriginPrice%3A745000%3BvoucherPrice%3A745000%3Btimestamp%3A1683215839838)')
        st.image(B660M, width=250)
        st.write(
            """
            If you're looking for a great deal on a motherboard, then the Gigabyte B660M DS3H is going to be extremely exciting. This budget-friendly motherboard is perfect for 12th and 13th Gen Intel processors, especially when you consider it comes with XMP profile supports, 2x M.2 slots, and onboard Wi-Fi.
            """
        )
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Q-Flash button
                - Works with 13th Gen processors
                - One of the best boards for the money
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Wi-Fi drivers must be downloaded
                """
             )

if "RAM" in add_selectbox:
     with st.container():
        st.title(":black[_RAM SELECTION_]")
        st.write(
            """ 
            BEST CPU RECOMMENDATION
            """
        )
        st.write('[TeamGroup T-Force Xtreem ARGB DDR4-3600 (2 x 8GB)](https://global.microless.com/product/teamgroup-t-force-xtreem-argb-16gb-2-x-8gb-288-pin-ddr4-sdram-ddr4-3600-pc4-28800-desktop-memory-tf10d416g3600hc18jdc01/?currency=usd)')
        st.image(TeamG, width=250)
        st.write(
            """
            TeamGroup did a great job with the Xtreem ARGB DDR4-3600 C14 memory kit -- It certainly ticks all the right boxes. The memory kit looks fantastic when lit up or powered down and performs equally well. The Xtreem ARGB is the fastest DDR4-3600 C14 memory kit that we've tested so far.
            """
        )

        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Superb performance
                - Attractive aesthetics
                - Good overclocker
                - Cheapest kit in its category
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Limited availability
                """
             )
        
    
        st.write('[Corsair Vengeance RGB Pro DDR4-3200 (4 x 8GB)](https://www.corsair.com/eu/en/Categories/Products/Memory/Vengeance-PRO-RGB-Black/p/CMW32GX4M4C3200C16)')
        st.image(Cor, width=250)
        st.write(
            """
Builders who put a premium on aesthetics face a tough choice between the best-looking and best-performance parts. Corsair brings a bit of both in its Vengeance RGB DDR4-3200 kit, providing four 8GB DIMMs (32GB total) at CAS 16 timings for a price that’s reasonably moderate given the recent market trends. And this kit isn’t all about looks; it has the goods where benchmarks are concerned, too.             """
        )

        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Excellent performance at rated (XMP) settings and across multiple data rates
                - Supports both Corsair and third-party RGB utilities
                - Reasonably priced
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Didn’t reach DDR4-4000
                - White light diffusers cast pastel hues
                """
            )
        
        st.write('[G.Skill Trident Z5 Neo RGB DDR5-6000 (2 x 16GB)](https://shopee.ph/G.-Skill-Trident-Z5-Neo-RGB-32GB(2x16GB)-DDR5-6000Mhz-CL36-36-36-96-1.35V-Desktop-Memory-i.89762129.21771571383?sp_atk=ea44dab3-3036-4e6b-af63-2b3f4421c9c9&xptdk=ea44dab3-3036-4e6b-af63-2b3f4421c9c9)')
        st.image(Gskill, width=250)
        st.write(
            """
            It's hard to find reasons not to like the Trident Z5 Neo RGB DDR5-6000 C30. The memory kit works immaculately out of the box and offers solid performance. That alone is enough to win the majority of buyers over. Looks, as usual, are subjective, but you can't dispute the Trident Z5 Neo RGB's premium exterior. Like its competition, G.Skill uses SK hynix M-die ICS for the memory kit, so some tweaking headroom is left in memory modules.
            """
        )

        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Superb performance
                - Cheaper than the competition
                - AMD EXPO certified
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Early adopter price
                """
            )
        
        st.write('[G.Skill Trident Z5 RGB DDR5-6000 (2 x 16GB)](https://shopee.ph/G.-Skill-Trident-Z5-Neo-RGB-32GB(2x16GB)-DDR5-6000Mhz-CL36-36-36-96-1.35V-Desktop-Memory-i.89762129.21771571383?sp_atk=e1873c61-d195-4f0d-b8a9-6f5586ce78af&xptdk=e1873c61-d195-4f0d-b8a9-6f5586ce78af)')
        st.image(Z5, width=250)
        st.write(
            """
The numbers speak for themselves. The G.Skill Trident Z5 RGB DDR5-6000 C36 is one of the fastest DDR5 memory kits that money can buy. It also has the best timings that you can find on a DDR5-6000 memory kit. The usage of Samsung's B-die integrated circuits means that the Trident Z5 RGB memory can run at tight timings even beyond the proclaimed DDR5-6000. As always, your ceiling will depend on the silicon lottery and how much voltage you're willing to pump into the memory.            """
        )

        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Excellent performance
                - Tight timings
                - Good OC potential
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Costs an arm and a leg
                """
            )
        
        st.write('[Corsair Vengeance DDR5-4800MHz](https://shopee.ph/G.-Skill-Trident-Z5-Neo-RGB-32GB(2x16GB)-DDR5-6000Mhz-CL36-36-36-96-1.35V-Desktop-Memory-i.89762129.21771571383?sp_atk=e1873c61-d195-4f0d-b8a9-6f5586ce78af&xptdk=e1873c61-d195-4f0d-b8a9-6f5586ce78af)')
        st.image(DDR5, width=250)
        st.write(
            """
If you want the speediest and latest RAM setup on the market then you'll have to spring for a set of DDR5 sticks. These normally don't come cheap but Corsair's latest iteration of its well-known Vengeance series of RAM is actually pretty competitively priced. While it's not the speediest set of DDR5 RAM on the market right now it's still pretty damn fast at a base clock speed of 4800MHz. It runs pretty cool too, so there's plenty of potential headroom if you're looking to overclock it alongside your other components.         )
            """
        )
        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Easy to overclock
                - Cheap (for DDR5)
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Not the highest clock speed out the box
                - Non-RGB version looks fairly pedestrian
                """
            )

if "Graphics Card" in add_selectbox:
     with st.container():
        st.title(":black[_GRAPHICS CARD SELECTION_]")
        st.write(
            """ 
            BEST GRAPHIC CARD RECOMMENDATION
            """
        )
        st.write('[AMD Radeon RX 6600 XT](https://shopee.ph/product/907199441/22408289181)')
        st.image(r6600xt , width=250)
        st.write(
            """
Compared to the RTX 3050, the 6600 XT is around 50% faster, give or take depending on the game. The 6600 XT does have some disadvantages, namely lack of DLSS support and poorer ray tracing performance. However, FSR (AMD's alternative to DLSS) is often in games that have DLSS and the ray tracing performance on the 3050 isn't great either, so unless you need an Nvidia GPU for a very specific feature, the 6600 XT is generally going to be a better purchase. You might also consider Intel's A750, which is about $50 cheaper and not much slower.            """
        )

        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Good performance at 1080p and 1440p
                - Supports ray tracing and FSR
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - $300 is barely budget
                """
             )
        
        st.write('[Nvidia GeForce GTX 1660 Super](https://stockx.com/nvidia-asus-tuf-gaming-geforce-gtx-1660-super-oc-6gb-graphics-card-tufgtx1660so6ggaming?country=US&currencyCode=USD&srsltid=AR57-fD4qm4NKMd8-VdgvLzqbC4F07PIiW7Rme30Ppmeq56sw9ouMo3O1zw)')
        st.image(G1660S , width=250)
        st.write(
            """
            When compared to the AMD competition, the GTX 1660 Super is a good bit faster than the Radeon RX 590, beating it overall by a 13% margin. But the Radeon's appeal is on pricing and that will determine which way you should go. If Nvidia does offer the 1660 Super at $230 then we’d purchase it over a $200 RX 590 and that was probably their intention all along.
            """
        )

        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Good performance at 1080p
                - Better value than 1660 Ti
                - Doesn't get too hot
                - Backplate, RGB, and idle fan stop features
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Missing RTX features
                - Only 1 HDMI and DisplayPort
                """
             )
            
        st.write('[Nvidia GeForce RTX 4070](https://www.lazada.com.ph/products/gigabyte-rtx-4070-windforce-oc-pn-gv-n4070wf3oc-12gd-i3730988783-s19675004842.html?spm=a2o4l.tm80167379.7779702790.1.a95fFatmFatmwd.a95fFatmFatmwd&priceCompare=skuId%3A19675004842%3Bsource%3Alazada-om%3Bsn%3A4b74b11e-b79f-4b88-a199-f7920e5f7e8c%3BoriginPrice%3A4039500%3BvoucherPrice%3A4039500%3Btimestamp%3A1683319376782)')
        st.image(R4070 , width=250)
        st.write(
            """
The Nvidia RTX 4070 Ti is easily the best GPU you can buy right now if what you're looking for is pure value for performance. Thanks to third-generation ray tracing cores, fourth-generation tensor cores, and advanced Nvidia Lovelace architecture, you get most of the best features of Nvidia's flagship GPUs of this generation without the exorbitant price tag.            """
        )

        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Excellent gaming performance
                - An excellent "budget" creative workstation GPU
                - Cheapest next-gen graphics card on the market
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - No Founders Edition
                - Only DisplayPort 1.4a
                - 12GB VRAM isn't great for 8K gaming
                """
             )
        
        st.write('[AMD Radeon RX 7900 XTX](https://www.bitworks.io/product/open-box-sapphire-nitro-amd-radeon-rx-7900-xtx-vapor-x-gaming-graphics-card/)')
        st.image(R7900 , width=250)
        st.write(
            """
The AMD Radeon RX 7900 XTX had a lot to prove when it hit the scene at the end of 2022, but it succeeds brilliantly in being the most powerful gaming GPU on the market for under $1,000 while outperforming Nvidia's RTX 4080 overall, which costs 20% more.
            """        
            )

        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Phenomenal performance
                - Well-priced for a premium card
                - Can fit in most cases
                - No 16-pin connector
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Ray tracing is still a generation behind Nvidia's newest cards
                - Just OK creative performance
                - Very power hungry
                """
             )
        
        st.write('[Nvidia GeForce RTX 3060 Ti](https://stockx.com/nvidia-geforce-rtx-3060-ti-graphics-card-900-1g142-2520-000?country=US&currencyCode=USD&srsltid=AR57-fBibnlZ4_fNmjD3hIdcf83K_JCkGSTd8IP_jndBsToRV1MQoIQJ2co)')
        st.image(R3060 , width=250)
        st.write(
            """
            Is AMD no longer the king of great value GPUs? The Nvidia GeForce RTX 3060 Ti threatens that claim with its price to performance ratio. One of the newer arrivals in the RTX 3000 line, this graphics card punches way above its weight class, delivering a performance that could rival the RTX 2080 Super while keeping its price tag incredibly affordable for most people. That’s with impressive ray tracing included. We've never seen 1080p gaming to be this good or this affordable. 
            """        
            )

        
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s to buy_]
                - Excellent 1080p performance
                - Ray tracing performance is solid
                - Stays cool
                """
            )

        with right_column:
            st.write("##")
            st.write(
                """
                :red[_Reason/s not to buy_]
                - Only entry-level 4K performance
                - Annoying 12-pin power connector
                """
             )







        

