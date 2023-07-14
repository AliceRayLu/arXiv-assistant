<template>
  <el-container
    style="position: absolute; top: 0; right: 0; bottom: 0; left: 0"
  >
    <el-aside width="20vw" style="background-color: #000000; height: 100vh">
      <el-row type="flex" justify="center" align="middle">
        <text style="color: #626aef; font-size: 4vh; margin-top: 2vh">
          arXiv-assistant
        </text>
      </el-row>
      <el-divider>
        <el-icon size="large"><Clock /></el-icon>
      </el-divider>
    </el-aside>
    <el-main>
      <div style="display: flex; width: 100%">
        <el-input
          placeholder="Type in whole sentences to search for papers."
          v-model="userInput"
          :prefix-icon="Search"
          style="display: inline-flex"
          clearable
        ></el-input>
        <el-button
          color="#626aef"
          style="display: inline-flex; margin-left: 0.5vw"
          @click="handleSend"
          >Send
        </el-button>
      </div>
      <div :key="isSend">
        <QandA :question="userInput" :is-send="isSend" />
      </div>
    </el-main>
  </el-container>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { Search, Clock } from "@element-plus/icons-vue";
import QandA from "@/components/QandA.vue";
import { useRouter } from "vue-router";

const router = useRouter();
const userInput = ref("");
let isSend = ref(false);

const handleSend = () => {
  isSend.value = true;
};
</script>

<style></style>
