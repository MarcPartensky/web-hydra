<script setup>
  // src/components/Form.vue

  const submitHandler = async (fields) => {
    // Let's pretend this is an ajax request:
    await new Promise((r) => setTimeout(r, 1000))
    console.log(fields)
  }
</script>

<template>
  <FormKit type="form" @submit="submitHandler">
    <FormKit type="text" label="Protocol" name="protocol" />
    <FormKit type="text" label="Interface" name="interface" />
    <FormKit type="number" label="Threads" name="threads" />
    <FormKit type="text" label="Ports" name="ports" />
  </FormKit>
</template>
