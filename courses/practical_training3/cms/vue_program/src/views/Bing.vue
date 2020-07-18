<template>
    <div class="home">
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
            <el-menu-item index="1">折线图</el-menu-item>
            <el-menu-item index="2">词云图</el-menu-item>
            <el-menu-item index="3">饼状图</el-menu-item>
        </el-menu>
        <h3 style="margin: 30px 0">岗位需求：城市占比</h3>
        <div id="container" style="max-width:800px;height:400px;margin:0 auto;border: orange 1px"></div>

    </div>
</template>

<script>

    // 显示饼状图的页面
    export default {
        name: 'Bing',
        data() {
            return {
                activeIndex: "3"
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
            this.axios.get("http://localhost:5000/pie").then(res=>{
                var data = res.data.data
                // TODO
            })
        }
    }
</script>
