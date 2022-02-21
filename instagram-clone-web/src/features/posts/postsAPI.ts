import { AxiosInstance } from '../../utils/axios'

export async function fetchPosts() {
  const response = await AxiosInstance.get('posts')
  if (response.status === 200) {
    return response
  }
  throw response
}
