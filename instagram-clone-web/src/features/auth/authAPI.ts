import { AxiosInstance } from '../../utils/axios'

export async function sendLogin(form: any) {
  const response = await AxiosInstance.post('login', form)
  console.log('sendLogin')
  console.log({ response })
  if (response.status === 200) {
    return response
  }
  throw response
}
