<script>
export default {
  name: 'EditableParagraph',
  props: ['label', 'modelValue'],
  emits: ['update:modelValue'],
  data() {
    return {
      content: this.modelValue
    };
  },
  watch: {
    content(newVal) {
      this.$emit('update:modelValue', newVal);
    },
    modelValue(newVal) {
      this.content = newVal;
    }
  }
};
</script>
