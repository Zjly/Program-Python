<template>
    <div class="home">
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
            <el-menu-item index="1">折线图</el-menu-item>
            <el-menu-item index="2">词云图</el-menu-item>
            <el-menu-item index="3">饼状图</el-menu-item>
        </el-menu>

        <h3 style="margin: 30px 0">一线城市平均工资</h3>
        <div id="container" style="max-width:800px;height:400px;margin:0 auto;border: orange 1px"></div>
    </div>
</template>

<script>

    // 显示折线图的页面
    export default {
        name: 'Home',
        data() {
           return {
               activeIndex : "1"
           }
        },
        methods: {
            // eslint-disable-next-line no-unused-vars
           handleSelect(key, keypath) {
               if(key == 1) {
                   this.$router.push("/")
               }
               if(key == 2) {
                   this.$router.push("/word")
               }
               if(key == 3) {
                   this.$router.push("/bing")
               }
           }
        },
        mounted() {
            this.axios.get("http://localhost:5000/line").then(res=>{
                var data = res.data.data()
                var city = new Array()
                var money = new Array()
                for(var i = 0; i < data.length; i++) {
                    city.push(data[i].name)
                    money.push(data[i].money)
                }
            })
        },
        Highcharts.chart("container", {
            title:{
                text:"一线城市平均工资"
            },
            yAxis:{
                title:{
                    text:"工资"
                }
            },
            xAxis:{
                title:{
                    text:"城市"
                },
                categories:city
            },
            series:[{
                name:"平均工资",
                data:money
            }]
        })
        components: {}
    }
</script>
